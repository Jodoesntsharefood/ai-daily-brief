#!/usr/bin/env python3

import argparse
import json
import os

from pathlib import Path

from urllib import request
from urllib import error


def main():

    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--html",
        required=True
    )


    parser.add_argument(
        "--date",
        required=True
    )


    parser.add_argument(
        "--subject",
        default=None
    )


    args = parser.parse_args()


    api_key = os.environ.get(
        "RESEND_API_KEY"
    )


    recipient = os.environ.get(
        "EMAIL_RECIPIENT"
    )


    sender = os.environ.get(

        "EMAIL_FROM",

        "AI Daily Brief <onboarding@resend.dev>"

    )


    if not api_key:

        raise SystemExit(

            "RESEND_API_KEY is not set."

        )


    if not recipient:

        raise SystemExit(

            "EMAIL_RECIPIENT is not set."

        )


    html_content = Path(

        args.html

    ).read_text(

        encoding="utf-8"

    )


    payload = {

        "from":

            sender,

        "to":

            [

                recipient

            ],

        "subject":

            args.subject

            or

            f"🤖 AI 日报 / AI Daily Brief — {args.date}",

        "html":

            html_content,

    }


    req = request.Request(

        "https://api.resend.com/emails",

        data=json.dumps(

            payload

        ).encode(

            "utf-8"

        ),

        headers={

            "Authorization":

                f"Bearer {api_key}",

            "Content-Type":

                "application/json",

        },

        method="POST",

    )


    try:

        with request.urlopen(

            req,

            timeout=30

        ) as response:


            response_body = response.read().decode(

                "utf-8"

            )


            print(

                "Email sent successfully."

            )


            print(

                response_body

            )


    except error.HTTPError as exc:


        detail = exc.read().decode(

            "utf-8",

            errors="replace"

        )


        raise SystemExit(

            f"Resend failed ({exc.code}): "

            f"{detail}"

        )


if __name__ == "__main__":

    main()