#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import csv
import argparse
import traceback
from jinja2 import Template

def main():

    parser = argparse.ArgumentParser()
    parser.prog = 'zscaler-config.bulder.py'
    parser.description = "Script builds configuraiton templates for Zscaler services."
    parser.epilog = "Please visit http://github.com/zscaler/zscaler-config-builder/ for updates."
    
    parser.add_argument('-C', 
                        dest='confpath',
                        required=False,
                        default=' ',
                        help='Configuration Path')
    parser.add_argument('-I', 
                        dest='input',
                        required=True,
                        default='template.csv',
                        help='CSV file with input variables')
    parser.add_argument('-T', 
                        dest='template',
                        required=True,
                        default='template.j2',
                        help='Jinja template file')
    parser.add_argument('-V', '--version', 
                        action='version',
                        version='%(prog)s 1.0')                    
    
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args()
        if not os.path.exists(args.input):
            parser.error("The file %s does not exist!  Please recheck the filename specfied" % args.input)
        if not os.path.exists(args.template):
            parser.error("The file %s does not exist!  Please recheck the filename specfied" % args.template)    
        cvs_variables = csv.DictReader(open(args.input))    
        #conf_path = args.confpath
        conf_path = ""

    for row in cvs_variables:
        vars = row
        configfile = "{}{}{}".format(conf_path, row["hostname"], ".conf")

        with open(args.template) as template_fh:
            template_format = template_fh.read()

        template = Template(template_format)

        fout = open(configfile, 'w')
        print fout

        fout.write((template.render(vars)))
        fout.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Ending...\n\n"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    print "Ending..."
    sys.exit(0)
