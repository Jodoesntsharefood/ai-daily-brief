#!/usr/bin/env python3

import argparse
import html
import json

from pathlib import Path


VALID_CATEGORIES = {
    "investment",
    "major_tech",
    "frontier",
    "regulation",
    "people",
}


CATEGORY_MARKERS = {

    "investment":
        "{{INVESTMENT_ITEMS}}",

    "major_tech":
        "{{MAJOR_TECH_ITEMS}}",

    "frontier":
        "{{FRONTIER_ITEMS}}",

    "regulation":
        "{{REGULATION_ITEMS}}",

    "people":
        "{{PEOPLE_ITEMS}}",

}


def escape(value):

    return html.escape(
        str(value),
        quote=True
    )


def validate(data):

    news = data.get("news", [])

    if len(news) != 10:

        raise ValueError(
            f"Exactly 10 news items are required. Got {len(news)}."
        )


    required_fields = {

        "id",
        "category",

        "title_cn",
        "title_en",

        "summary_cn",
        "summary_en",

        "source",
        "url",
        "date",

    }


    seen_ids = set()


    for index, item in enumerate(news, start=1):

        missing = required_fields - set(item.keys())


        if missing:

            raise ValueError(
                f"Item {index} is missing fields: {sorted(missing)}"
            )


        if item["category"] not in VALID_CATEGORIES:

            raise ValueError(
                f"Item {index} has invalid category: "
                f"{item['category']}"
            )


        if item["id"] in seen_ids:

            raise ValueError(
                f"Duplicate news ID: {item['id']}"
            )


        seen_ids.add(
            item["id"]
        )


        url = str(
            item["url"]
        )


        if not url.startswith(
            ("https://", "http://")
        ):

            raise ValueError(
                f"Item {index} has invalid URL."
            )


def render_executive_map(item):

    return f"""
<tr>

<td style="
width:44px;
padding:10px 8px;
background:#FFFFFF;
border:1px solid #E8F0F8;
border-right:0;
border-radius:9px 0 0 9px;
text-align:center;
">

<span style="
display:inline-block;
min-width:23px;
padding:3px 0;
border-radius:999px;
background:#EAF3FC;
color:#2C6FA3;
font-weight:700;
font-size:12px;
">

{int(item["id"]):02d}

</span>

</td>


<td style="
padding:10px;
background:#FFFFFF;
border:1px solid #E8F0F8;
border-left:0;
border-radius:0 9px 9px 0;
">

<b>

{escape(item["title_cn"])}

</b>

<br>

<span style="color:#667788;">

{escape(item["title_en"])}

</span>

</td>

</tr>
"""


def render_news_item(item, is_last):

    divider = ""


    if not is_last:

        divider = """

border-bottom:1px solid #F0F0F0;
padding-bottom:14px;

"""


    return f"""
<div style="
{divider}
margin-bottom:18px;
">


<p style="
margin:0 0 4px;
font-size:15.5px;
line-height:1.5;
font-weight:700;
color:#1A1A1A;
">

{escape(item["title_cn"])}

</p>


<p style="
margin:0 0 8px;
font-size:13px;
line-height:1.55;
color:#666666;
font-style:italic;
">

{escape(item["title_en"])}

</p>


<p style="
margin:0 0 8px;
font-size:14px;
line-height:1.75;
color:#444444;
">

{escape(item["summary_cn"])}

</p>


<p style="
margin:0 0 8px;
font-size:13.5px;
line-height:1.7;
color:#666666;
">

{escape(item["summary_en"])}

</p>


<p style="
margin:0;
font-size:12px;
line-height:1.5;
color:#888888;
">

来源 / Source:

<a
href="{escape(item["url"])}"

style="
color:#4A90D9;
text-decoration:none;
"

>

{escape(item["source"])}

</a>

｜

日期 / Date:

{escape(item["date"])}

</p>


</div>
"""


def main():

    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--input",
        required=True
    )


    parser.add_argument(
        "--template",
        required=True
    )


    parser.add_argument(
        "--output",
        required=True
    )


    args = parser.parse_args()


    input_path = Path(
        args.input
    )


    template_path = Path(
        args.template
    )


    output_path = Path(
        args.output
    )


    data = json.loads(

        input_path.read_text(
            encoding="utf-8"
        )

    )


    validate(
        data
    )


    rendered = template_path.read_text(
        encoding="utf-8"
    )


    rendered = rendered.replace(

        "{{BRIEF_DATE}}",

        escape(
            data["brief_date"]
        )

    )


    rendered = rendered.replace(

        "{{BRIEF_DATE_BILINGUAL}}",

        escape(
            data["brief_date_bilingual"]
        )

    )


    news = sorted(

        data["news"],

        key=lambda item:

        int(
            item["id"]
        )

    )


    executive_map_html = "\n".join(

        render_executive_map(
            item
        )

        for item in news

    )


    rendered = rendered.replace(

        "{{EXECUTIVE_MAP}}",

        executive_map_html

    )


    for category, marker in CATEGORY_MARKERS.items():

        items = [

            item

            for item in news

            if item["category"] == category

        ]


        category_html = "\n".join(

            render_news_item(

                item,

                index == len(items) - 1

            )

            for index, item

            in enumerate(
                items
            )

        )


        rendered = rendered.replace(

            marker,

            category_html

        )


    all_markers = [

        "{{BRIEF_DATE}}",

        "{{BRIEF_DATE_BILINGUAL}}",

        "{{EXECUTIVE_MAP}}",

        *CATEGORY_MARKERS.values(),

    ]


    unresolved = [

        marker

        for marker in all_markers

        if marker in rendered

    ]


    if unresolved:

        raise ValueError(

            "Unresolved template markers: "

            + ", ".join(
                unresolved
            )

        )


    output_path.parent.mkdir(

        parents=True,

        exist_ok=True

    )


    output_path.write_text(

        rendered,

        encoding="utf-8"

    )


    print(

        f"HTML generated: {output_path}"

    )


if __name__ == "__main__":

    main()