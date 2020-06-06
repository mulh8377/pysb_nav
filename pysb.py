
import argparse
import src.GUI.window as GUI_WINDOW
import src.CLI.main as CLI_WINDOW
import src.WEB.main as REF_WINDOW
#import src.action as pysb_ref

import asyncio

async def window():
    await GUI_WINDOW.run()

async def cli():
    print(CLI_WINDOW.run(command="start"))

async def ref():
    print(REF_WINDOW.run(command="start"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--win", required=False)
    parser.add_argument("--web", required=False)
    parser.add_argument("--cli", required=False)

    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    if args.win:
        loop.run_until_complete(window())
    if args.web:
        loop.run_until_complete(ref())
    if args.cli:
        loop.run_until_complete(cli())