# Zscaler Config Builder 

_Zscaler Config Builder_ is a Python script for building CE/CPE device configs to support Zscaler Internet Access (ZIA).  The user is ***NOT*** required: (a) to be a "Software Programmer™", (b) have sophisticated knowledge of the operating systems this tool can build configurations for.  

## INSTALLATION

### Installing Dependancies using PIP

Installation requires Python 2.6 or 2.7 or >=3.4 and associated `pip` tool

        pip install jinja2 argparse

Installing from Git is also supported (OS must have git installed).

        To install the latest MASTER code
        pip install git+https://github.com/eparra/zscaler-config-builder.git
        -or-
        To install a specific version, branch, tag, etc.
        pip install git+https://github.com/eparra/zscaler-config-builder.git@<branch,tag,commit>

## USAGE

**CLI Syntax**

        ./zscaler-config-builder.py -I <CSV FILE> -T <JINJA TEMPLATE> 
        
**Example**

        ./zscaler-config-builder.py -I zscaler-junos-srx-gre.csv -T zscaler-junos-srx-gre.j2

## LICENSE

MIT

## CONTRIBUTORS

We welcome other contributors.  

*Contributors:*

[Eddie Parra](https://github.com/eparra)
