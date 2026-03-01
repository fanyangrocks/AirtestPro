# -*- coding: utf-8 -*-
from airtest_pro.cli.parser import get_parser


def main(argv=None):
    ap = get_parser()
    args = ap.parse_args(argv)
    if args.action == "info":
        from AirtestPro.cli.info import get_script_info
        print(get_script_info(args.script))
    elif args.action == "report":
        from AirtestPro.report.report import main as report_main
        report_main(args)
    elif args.action == "run":
        from AirtestPro.cli.runner import run_script
        run_script(args)
    elif args.action == "version":
        from AirtestPro.utils.version import show_version
        show_version()
    else:
        ap.print_help()


if __name__ == '__main__':
    main()
