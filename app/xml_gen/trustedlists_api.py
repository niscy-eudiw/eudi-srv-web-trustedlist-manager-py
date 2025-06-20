# coding: latin-1
###############################################################################
# Copyright (c) 2023 European Commission
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Tue Dec  3 15:28:20 2024 by generateDS.py version 2.44.3.
# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'trustedlists_api.py')
#   ('-s', 'trustedlists_sub.py')
#   ('--super', 'trustedlists_api')
#
# Command line arguments:
#   ts_119612v020101_xsd_modified.xsd
#
# Command line:
#   generateDS.py -o "trustedlists_api.py" -s "trustedlists_sub.py" --super="trustedlists_api" ts_119612v020101_xsd_modified.xsd
#
# Current working directory (os.getcwd()):
#   trusted_lists
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile('(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            value = ('%.15f' % float(input_data)).rstrip('0')
            if value.endswith('.'):
                value += '0'
            return value
    
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            input_data = input_data.strip()
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%SZ')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'{.*}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    s1 = s1.replace('\n', '&#10;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


#
# Start enum classes
#
class QualifierType1(str, Enum):
    OID_AS_URI='OIDAsURI'
    OID_AS_URN='OIDAsURN'


class assertType(str, Enum):
    ALL='all'
    AT_LEAST_ONE='atLeastOne'
    NONE='none'


class nameType(str, Enum):
    DIGITAL_SIGNATURE='digitalSignature'
    NON_REPUDIATION='nonRepudiation'
    KEY_ENCIPHERMENT='keyEncipherment'
    DATA_ENCIPHERMENT='dataEncipherment'
    KEY_AGREEMENT='keyAgreement'
    KEY_CERT_SIGN='keyCertSign'
    CRL_SIGN='crlSign'
    ENCIPHER_ONLY='encipherOnly'
    DECIPHER_ONLY='decipherOnly'


#
# Start data representation classes
#
class InternationalNamesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if Name is None:
            self.Name = []
        else:
            self.Name = Name
        self.Name_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InternationalNamesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InternationalNamesType.subclass:
            return InternationalNamesType.subclass(*args_, **kwargs_)
        else:
            return InternationalNamesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def add_Name(self, value):
        self.Name.append(value)
    def insert_Name_at(self, index, value):
        self.Name.insert(index, value)
    def replace_Name_at(self, index, value):
        self.Name[index] = value
    def has__content(self):
        if (
            self.Name
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='InternationalNamesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InternationalNamesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InternationalNamesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InternationalNamesType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InternationalNamesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InternationalNamesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='InternationalNamesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Name_ in self.Name:
            namespaceprefix_ = self.Name_nsprefix_ + ':' if (UseCapturedNS_ and self.Name_nsprefix_) else ''
            Name_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Name', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Name':
            obj_ = MultiLangNormStringType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name.append(obj_)
            obj_.original_tagname_ = 'Name'
# end class InternationalNamesType


class MultiLangNormStringType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lang=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.lang = _cast(None, lang)
        self.lang_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MultiLangNormStringType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MultiLangNormStringType.subclass:
            return MultiLangNormStringType.subclass(*args_, **kwargs_)
        else:
            return MultiLangNormStringType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_NonEmptyNormalizedString(self, value):
        result = True
        # Validate type NonEmptyNormalizedString, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NonEmptyNormalizedString' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='MultiLangNormStringType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MultiLangNormStringType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MultiLangNormStringType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MultiLangNormStringType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MultiLangNormStringType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' xml:lang=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lang), input_name='lang')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='MultiLangNormStringType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class MultiLangNormStringType


class MultiLangStringType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lang=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.lang = _cast(None, lang)
        self.lang_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MultiLangStringType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MultiLangStringType.subclass:
            return MultiLangStringType.subclass(*args_, **kwargs_)
        else:
            return MultiLangStringType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_NonEmptyString(self, value):
        result = True
        # Validate type NonEmptyString, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NonEmptyString' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='MultiLangStringType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MultiLangStringType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MultiLangStringType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MultiLangStringType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MultiLangStringType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' xml:lang=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lang), input_name='lang')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='MultiLangStringType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class MultiLangStringType


class AddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PostalAddresses=None, ElectronicAddress=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.PostalAddresses = PostalAddresses
        self.PostalAddresses_nsprefix_ = "tsl"
        self.ElectronicAddress = ElectronicAddress
        self.ElectronicAddress_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AddressType.subclass:
            return AddressType.subclass(*args_, **kwargs_)
        else:
            return AddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PostalAddresses(self):
        return self.PostalAddresses
    def set_PostalAddresses(self, PostalAddresses):
        self.PostalAddresses = PostalAddresses
    def get_ElectronicAddress(self):
        return self.ElectronicAddress
    def set_ElectronicAddress(self, ElectronicAddress):
        self.ElectronicAddress = ElectronicAddress
    def has__content(self):
        if (
            self.PostalAddresses is not None or
            self.ElectronicAddress is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='AddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AddressType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='AddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PostalAddresses is not None:
            namespaceprefix_ = self.PostalAddresses_nsprefix_ + ':' if (UseCapturedNS_ and self.PostalAddresses_nsprefix_) else ''
            self.PostalAddresses.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='PostalAddresses', pretty_print=pretty_print)
        if self.ElectronicAddress is not None:
            namespaceprefix_ = self.ElectronicAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.ElectronicAddress_nsprefix_) else ''
            self.ElectronicAddress.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ElectronicAddress', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PostalAddresses':
            obj_ = PostalAddressListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PostalAddresses = obj_
            obj_.original_tagname_ = 'PostalAddresses'
        elif nodeName_ == 'ElectronicAddress':
            obj_ = ElectronicAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElectronicAddress = obj_
            obj_.original_tagname_ = 'ElectronicAddress'
# end class AddressType


class PostalAddressListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PostalAddress=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if PostalAddress is None:
            self.PostalAddress = []
        else:
            self.PostalAddress = PostalAddress
        self.PostalAddress_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PostalAddressListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PostalAddressListType.subclass:
            return PostalAddressListType.subclass(*args_, **kwargs_)
        else:
            return PostalAddressListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PostalAddress(self):
        return self.PostalAddress
    def set_PostalAddress(self, PostalAddress):
        self.PostalAddress = PostalAddress
    def add_PostalAddress(self, value):
        self.PostalAddress.append(value)
    def insert_PostalAddress_at(self, index, value):
        self.PostalAddress.insert(index, value)
    def replace_PostalAddress_at(self, index, value):
        self.PostalAddress[index] = value
    def has__content(self):
        if (
            self.PostalAddress
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PostalAddressListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PostalAddressListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PostalAddressListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PostalAddressListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PostalAddressListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PostalAddressListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PostalAddressListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for PostalAddress_ in self.PostalAddress:
            namespaceprefix_ = self.PostalAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.PostalAddress_nsprefix_) else ''
            PostalAddress_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='PostalAddress', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PostalAddress':
            obj_ = PostalAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PostalAddress.append(obj_)
            obj_.original_tagname_ = 'PostalAddress'
# end class PostalAddressListType


class PostalAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lang=None, StreetAddress=None, Locality=None, StateOrProvince=None, PostalCode=None, CountryName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.lang = _cast(None, lang)
        self.lang_nsprefix_ = None
        self.StreetAddress = StreetAddress
        self.validate_NonEmptyString(self.StreetAddress)
        self.StreetAddress_nsprefix_ = "tsl"
        self.Locality = Locality
        self.validate_NonEmptyString(self.Locality)
        self.Locality_nsprefix_ = "tsl"
        self.StateOrProvince = StateOrProvince
        self.validate_NonEmptyString(self.StateOrProvince)
        self.StateOrProvince_nsprefix_ = "tsl"
        self.PostalCode = PostalCode
        self.validate_NonEmptyString(self.PostalCode)
        self.PostalCode_nsprefix_ = "tsl"
        self.CountryName = CountryName
        self.validate_NonEmptyString(self.CountryName)
        self.CountryName_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PostalAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PostalAddressType.subclass:
            return PostalAddressType.subclass(*args_, **kwargs_)
        else:
            return PostalAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_StreetAddress(self):
        return self.StreetAddress
    def set_StreetAddress(self, StreetAddress):
        self.StreetAddress = StreetAddress
    def get_Locality(self):
        return self.Locality
    def set_Locality(self, Locality):
        self.Locality = Locality
    def get_StateOrProvince(self):
        return self.StateOrProvince
    def set_StateOrProvince(self, StateOrProvince):
        self.StateOrProvince = StateOrProvince
    def get_PostalCode(self):
        return self.PostalCode
    def set_PostalCode(self, PostalCode):
        self.PostalCode = PostalCode
    def get_CountryName(self):
        return self.CountryName
    def set_CountryName(self, CountryName):
        self.CountryName = CountryName
    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def validate_NonEmptyString(self, value):
        result = True
        # Validate type NonEmptyString, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NonEmptyString' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.StreetAddress is not None or
            self.Locality is not None or
            self.StateOrProvince is not None or
            self.PostalCode is not None or
            self.CountryName is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PostalAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PostalAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PostalAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PostalAddressType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PostalAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PostalAddressType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' xml:lang=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lang), input_name='lang')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PostalAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.StreetAddress is not None:
            namespaceprefix_ = self.StreetAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.StreetAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStreetAddress>%s</%sStreetAddress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StreetAddress), input_name='StreetAddress')), namespaceprefix_ , eol_))
        if self.Locality is not None:
            namespaceprefix_ = self.Locality_nsprefix_ + ':' if (UseCapturedNS_ and self.Locality_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLocality>%s</%sLocality>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Locality), input_name='Locality')), namespaceprefix_ , eol_))
        if self.StateOrProvince is not None:
            namespaceprefix_ = self.StateOrProvince_nsprefix_ + ':' if (UseCapturedNS_ and self.StateOrProvince_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStateOrProvince>%s</%sStateOrProvince>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StateOrProvince), input_name='StateOrProvince')), namespaceprefix_ , eol_))
        if self.PostalCode is not None:
            namespaceprefix_ = self.PostalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.PostalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostalCode>%s</%sPostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PostalCode), input_name='PostalCode')), namespaceprefix_ , eol_))
        if self.CountryName is not None:
            namespaceprefix_ = self.CountryName_nsprefix_ + ':' if (UseCapturedNS_ and self.CountryName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCountryName>%s</%sCountryName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CountryName), input_name='CountryName')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'StreetAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StreetAddress')
            value_ = self.gds_validate_string(value_, node, 'StreetAddress')
            self.StreetAddress = value_
            self.StreetAddress_nsprefix_ = child_.prefix
            # validate type NonEmptyString
            self.validate_NonEmptyString(self.StreetAddress)
        elif nodeName_ == 'Locality':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Locality')
            value_ = self.gds_validate_string(value_, node, 'Locality')
            self.Locality = value_
            self.Locality_nsprefix_ = child_.prefix
            # validate type NonEmptyString
            self.validate_NonEmptyString(self.Locality)
        elif nodeName_ == 'StateOrProvince':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StateOrProvince')
            value_ = self.gds_validate_string(value_, node, 'StateOrProvince')
            self.StateOrProvince = value_
            self.StateOrProvince_nsprefix_ = child_.prefix
            # validate type NonEmptyString
            self.validate_NonEmptyString(self.StateOrProvince)
        elif nodeName_ == 'PostalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PostalCode')
            value_ = self.gds_validate_string(value_, node, 'PostalCode')
            self.PostalCode = value_
            self.PostalCode_nsprefix_ = child_.prefix
            # validate type NonEmptyString
            self.validate_NonEmptyString(self.PostalCode)
        elif nodeName_ == 'CountryName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CountryName')
            value_ = self.gds_validate_string(value_, node, 'CountryName')
            self.CountryName = value_
            self.CountryName_nsprefix_ = child_.prefix
            # validate type NonEmptyString
            self.validate_NonEmptyString(self.CountryName)
# end class PostalAddressType


class ElectronicAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if URI is None:
            self.URI = []
        else:
            self.URI = URI
        self.URI_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ElectronicAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ElectronicAddressType.subclass:
            return ElectronicAddressType.subclass(*args_, **kwargs_)
        else:
            return ElectronicAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def add_URI(self, value):
        self.URI.append(value)
    def insert_URI_at(self, index, value):
        self.URI.insert(index, value)
    def replace_URI_at(self, index, value):
        self.URI[index] = value
    def has__content(self):
        if (
            self.URI
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ElectronicAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ElectronicAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ElectronicAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ElectronicAddressType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ElectronicAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ElectronicAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ElectronicAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for URI_ in self.URI:
            namespaceprefix_ = self.URI_nsprefix_ + ':' if (UseCapturedNS_ and self.URI_nsprefix_) else ''
            URI_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='URI', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'URI':
            obj_ = NonEmptyMultiLangURIType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.URI.append(obj_)
            obj_.original_tagname_ = 'URI'
# end class ElectronicAddressType


class AnyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnyType.subclass:
            return AnyType.subclass(*args_, **kwargs_)
        else:
            return AnyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def has__content(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='AnyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnyType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnyType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='AnyType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class AnyType


class ExtensionType(AnyType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = AnyType
    def __init__(self, anytypeobjs_=None, Critical=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        super(globals().get("ExtensionType"), self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
        self.Critical = _cast(bool, Critical)
        self.Critical_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExtensionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExtensionType.subclass:
            return ExtensionType.subclass(*args_, **kwargs_)
        else:
            return ExtensionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Critical(self):
        return self.Critical
    def set_Critical(self, Critical):
        self.Critical = Critical
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_ or
            super(ExtensionType, self).has__content()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ExtensionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExtensionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExtensionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExtensionType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExtensionType'):
        super(ExtensionType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExtensionType')
        if self.Critical is not None and 'Critical' not in already_processed:
            already_processed.add('Critical')
            outfile.write(' Critical="%s"' % self.gds_format_boolean(self.Critical, input_name='Critical'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ExtensionType', fromsubclass_=False, pretty_print=True):
        super(ExtensionType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Critical', node)
        if value is not None and 'Critical' not in already_processed:
            already_processed.add('Critical')
            if value in ('true', '1'):
                self.Critical = True
            elif value in ('false', '0'):
                self.Critical = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(ExtensionType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(ExtensionType, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class ExtensionType


class ExtensionsListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Extension=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if Extension is None:
            self.Extension = []
        else:
            self.Extension = Extension
        self.Extension_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExtensionsListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExtensionsListType.subclass:
            return ExtensionsListType.subclass(*args_, **kwargs_)
        else:
            return ExtensionsListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Extension(self):
        return self.Extension
    def set_Extension(self, Extension):
        self.Extension = Extension
    def add_Extension(self, value):
        self.Extension.append(value)
    def insert_Extension_at(self, index, value):
        self.Extension.insert(index, value)
    def replace_Extension_at(self, index, value):
        self.Extension[index] = value
    def has__content(self):
        if (
            self.Extension
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ExtensionsListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExtensionsListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExtensionsListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExtensionsListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ExtensionsListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExtensionsListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ExtensionsListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Extension_ in self.Extension:
            namespaceprefix_ = self.Extension_nsprefix_ + ':' if (UseCapturedNS_ and self.Extension_nsprefix_) else ''
            Extension_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='Extension', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Extension':
            obj_ = ExtensionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Extension.append(obj_)
            obj_.original_tagname_ = 'Extension'
# end class ExtensionsListType


class NonEmptyMultiLangURIListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if URI is None:
            self.URI = []
        else:
            self.URI = URI
        self.URI_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonEmptyMultiLangURIListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonEmptyMultiLangURIListType.subclass:
            return NonEmptyMultiLangURIListType.subclass(*args_, **kwargs_)
        else:
            return NonEmptyMultiLangURIListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def add_URI(self, value):
        self.URI.append(value)
    def insert_URI_at(self, index, value):
        self.URI.insert(index, value)
    def replace_URI_at(self, index, value):
        self.URI[index] = value
    def has__content(self):
        if (
            self.URI
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyMultiLangURIListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonEmptyMultiLangURIListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonEmptyMultiLangURIListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonEmptyMultiLangURIListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonEmptyMultiLangURIListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonEmptyMultiLangURIListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyMultiLangURIListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for URI_ in self.URI:
            namespaceprefix_ = self.URI_nsprefix_ + ':' if (UseCapturedNS_ and self.URI_nsprefix_) else ''
            URI_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='URI', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'URI':
            obj_ = NonEmptyMultiLangURIType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.URI.append(obj_)
            obj_.original_tagname_ = 'URI'
# end class NonEmptyMultiLangURIListType


class NonEmptyURIListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if URI is None:
            self.URI = []
        else:
            self.URI = URI
        self.URI_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonEmptyURIListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonEmptyURIListType.subclass:
            return NonEmptyURIListType.subclass(*args_, **kwargs_)
        else:
            return NonEmptyURIListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def add_URI(self, value):
        self.URI.append(value)
    def insert_URI_at(self, index, value):
        self.URI.insert(index, value)
    def replace_URI_at(self, index, value):
        self.URI[index] = value
    def has__content(self):
        if (
            self.URI
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyURIListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonEmptyURIListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonEmptyURIListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonEmptyURIListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonEmptyURIListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonEmptyURIListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyURIListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for URI_ in self.URI:
            namespaceprefix_ = self.URI_nsprefix_ + ':' if (UseCapturedNS_ and self.URI_nsprefix_) else ''
            URI_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='URI', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'URI':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.URI.append(obj_)
            obj_.original_tagname_ = 'URI'
# end class NonEmptyURIListType


class TrustStatusListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TSLTag=None, Id=None, SchemeInformation=None, TrustServiceProviderList=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.TSLTag = _cast(None, TSLTag)
        self.TSLTag_nsprefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SchemeInformation = SchemeInformation
        self.SchemeInformation_nsprefix_ = "tsl"
        self.TrustServiceProviderList = TrustServiceProviderList
        self.TrustServiceProviderList_nsprefix_ = "tsl"
        self.Signature = Signature
        self.Signature_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrustStatusListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrustStatusListType.subclass:
            return TrustStatusListType.subclass(*args_, **kwargs_)
        else:
            return TrustStatusListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SchemeInformation(self):
        return self.SchemeInformation
    def set_SchemeInformation(self, SchemeInformation):
        self.SchemeInformation = SchemeInformation
    def get_TrustServiceProviderList(self):
        return self.TrustServiceProviderList
    def set_TrustServiceProviderList(self, TrustServiceProviderList):
        self.TrustServiceProviderList = TrustServiceProviderList
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def get_TSLTag(self):
        return self.TSLTag
    def set_TSLTag(self, TSLTag):
        self.TSLTag = TSLTag
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def has__content(self):
        if (
            self.SchemeInformation is not None or
            self.TrustServiceProviderList is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:tslx="http://uri.etsi.org/02231/v2/additionaltypes#" ', name_='TrustServiceStatusList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrustServiceStatusList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TrustServiceStatusList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrustServiceStatusList')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrustServiceStatusList', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TrustServiceStatusList'):
        if self.TSLTag is not None and 'TSLTag' not in already_processed:
            already_processed.add('TSLTag')
            outfile.write(' TSLTag=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.TSLTag), input_name='TSLTag')), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:tslx="http://uri.etsi.org/02231/v2/additionaltypes#"', name_='TrustServiceStatusList', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SchemeInformation is not None:
            namespaceprefix_ = self.SchemeInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeInformation_nsprefix_) else ''
            self.SchemeInformation.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='SchemeInformation', pretty_print=pretty_print)
        if self.TrustServiceProviderList is not None:
            namespaceprefix_ = self.TrustServiceProviderList_nsprefix_ + ':' if (UseCapturedNS_ and self.TrustServiceProviderList_nsprefix_) else ''
            self.TrustServiceProviderList.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='TrustServiceProviderList', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('TSLTag', node)
        if value is not None and 'TSLTag' not in already_processed:
            already_processed.add('TSLTag')
            self.TSLTag = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SchemeInformation':
            obj_ = TSLSchemeInformationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeInformation = obj_
            obj_.original_tagname_ = 'SchemeInformation'
        elif nodeName_ == 'TrustServiceProviderList':
            obj_ = TrustServiceProviderListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TrustServiceProviderList = obj_
            obj_.original_tagname_ = 'TrustServiceProviderList'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class TrustServiceStatusListType


class TrustServiceProviderListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TrustServiceProvider=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if TrustServiceProvider is None:
            self.TrustServiceProvider = []
        else:
            self.TrustServiceProvider = TrustServiceProvider
        self.TrustServiceProvider_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrustServiceProviderListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrustServiceProviderListType.subclass:
            return TrustServiceProviderListType.subclass(*args_, **kwargs_)
        else:
            return TrustServiceProviderListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TrustServiceProvider(self):
        return self.TrustServiceProvider
    def set_TrustServiceProvider(self, TrustServiceProvider):
        self.TrustServiceProvider = TrustServiceProvider
    def add_TrustServiceProvider(self, value):
        self.TrustServiceProvider.append(value)
    def insert_TrustServiceProvider_at(self, index, value):
        self.TrustServiceProvider.insert(index, value)
    def replace_TrustServiceProvider_at(self, index, value):
        self.TrustServiceProvider[index] = value
    def has__content(self):
        if (
            self.TrustServiceProvider
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TrustServiceProviderListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrustServiceProviderListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TrustServiceProviderListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrustServiceProviderListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrustServiceProviderListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TrustServiceProviderListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TrustServiceProviderListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TrustServiceProvider_ in self.TrustServiceProvider:
            namespaceprefix_ = self.TrustServiceProvider_nsprefix_ + ':' if (UseCapturedNS_ and self.TrustServiceProvider_nsprefix_) else ''
            TrustServiceProvider_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='TrustServiceProvider', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TrustServiceProvider':
            obj_ = TSPType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TrustServiceProvider.append(obj_)
            obj_.original_tagname_ = 'TrustServiceProvider'
# end class TrustServiceProviderListType


class TSLSchemeInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TSLVersionIdentifier=None, TSLSequenceNumber=None, TSLType=None, SchemeOperatorName=None, SchemeOperatorAddress=None, SchemeName=None, SchemeInformationURI=None, StatusDeterminationApproach=None, SchemeTypeCommunityRules=None, SchemeTerritory=None, PolicyOrLegalNotice=None, HistoricalInformationPeriod=None, PointersToOtherTSL=None, ListIssueDateTime=None, NextUpdate=None, DistributionPoints=None, SchemeExtensions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TSLVersionIdentifier = TSLVersionIdentifier
        self.TSLVersionIdentifier_nsprefix_ = None
        self.TSLSequenceNumber = TSLSequenceNumber
        self.TSLSequenceNumber_nsprefix_ = None
        self.TSLType = TSLType
        self.TSLType_nsprefix_ = "tsl"
        self.SchemeOperatorName = SchemeOperatorName
        self.SchemeOperatorName_nsprefix_ = "tsl"
        self.SchemeOperatorAddress = SchemeOperatorAddress
        self.SchemeOperatorAddress_nsprefix_ = "tsl"
        self.SchemeName = SchemeName
        self.SchemeName_nsprefix_ = "tsl"
        self.SchemeInformationURI = SchemeInformationURI
        self.SchemeInformationURI_nsprefix_ = "tsl"
        self.StatusDeterminationApproach = StatusDeterminationApproach
        self.StatusDeterminationApproach_nsprefix_ = "tsl"
        self.SchemeTypeCommunityRules = SchemeTypeCommunityRules
        self.SchemeTypeCommunityRules_nsprefix_ = "tsl"
        self.SchemeTerritory = SchemeTerritory
        self.SchemeTerritory_nsprefix_ = "tsl"
        self.PolicyOrLegalNotice = PolicyOrLegalNotice
        self.PolicyOrLegalNotice_nsprefix_ = "tsl"
        self.HistoricalInformationPeriod = HistoricalInformationPeriod
        self.HistoricalInformationPeriod_nsprefix_ = None
        self.PointersToOtherTSL = PointersToOtherTSL
        self.PointersToOtherTSL_nsprefix_ = "tsl"
        if isinstance(ListIssueDateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(ListIssueDateTime, '%Y-%m-%dT%H:%M:%SZ')
        else:
            initvalue_ = ListIssueDateTime
        self.ListIssueDateTime = initvalue_
        self.ListIssueDateTime_nsprefix_ = None
        self.NextUpdate = NextUpdate
        self.NextUpdate_nsprefix_ = "tsl"
        self.DistributionPoints = DistributionPoints
        self.DistributionPoints_nsprefix_ = "tsl"
        self.SchemeExtensions = SchemeExtensions
        self.SchemeExtensions_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSLSchemeInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSLSchemeInformationType.subclass:
            return TSLSchemeInformationType.subclass(*args_, **kwargs_)
        else:
            return TSLSchemeInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TSLVersionIdentifier(self):
        return self.TSLVersionIdentifier
    def set_TSLVersionIdentifier(self, TSLVersionIdentifier):
        self.TSLVersionIdentifier = TSLVersionIdentifier
    def get_TSLSequenceNumber(self):
        return self.TSLSequenceNumber
    def set_TSLSequenceNumber(self, TSLSequenceNumber):
        self.TSLSequenceNumber = TSLSequenceNumber
    def get_TSLType(self):
        return self.TSLType
    def set_TSLType(self, TSLType):
        self.TSLType = TSLType
    def get_SchemeOperatorName(self):
        return self.SchemeOperatorName
    def set_SchemeOperatorName(self, SchemeOperatorName):
        self.SchemeOperatorName = SchemeOperatorName
    def get_SchemeOperatorAddress(self):
        return self.SchemeOperatorAddress
    def set_SchemeOperatorAddress(self, SchemeOperatorAddress):
        self.SchemeOperatorAddress = SchemeOperatorAddress
    def get_SchemeName(self):
        return self.SchemeName
    def set_SchemeName(self, SchemeName):
        self.SchemeName = SchemeName
    def get_SchemeInformationURI(self):
        return self.SchemeInformationURI
    def set_SchemeInformationURI(self, SchemeInformationURI):
        self.SchemeInformationURI = SchemeInformationURI
    def get_StatusDeterminationApproach(self):
        return self.StatusDeterminationApproach
    def set_StatusDeterminationApproach(self, StatusDeterminationApproach):
        self.StatusDeterminationApproach = StatusDeterminationApproach
    def get_SchemeTypeCommunityRules(self):
        return self.SchemeTypeCommunityRules
    def set_SchemeTypeCommunityRules(self, SchemeTypeCommunityRules):
        self.SchemeTypeCommunityRules = SchemeTypeCommunityRules
    def get_SchemeTerritory(self):
        return self.SchemeTerritory
    def set_SchemeTerritory(self, SchemeTerritory):
        self.SchemeTerritory = SchemeTerritory
    def get_PolicyOrLegalNotice(self):
        return self.PolicyOrLegalNotice
    def set_PolicyOrLegalNotice(self, PolicyOrLegalNotice):
        self.PolicyOrLegalNotice = PolicyOrLegalNotice
    def get_HistoricalInformationPeriod(self):
        return self.HistoricalInformationPeriod
    def set_HistoricalInformationPeriod(self, HistoricalInformationPeriod):
        self.HistoricalInformationPeriod = HistoricalInformationPeriod
    def get_PointersToOtherTSL(self):
        return self.PointersToOtherTSL
    def set_PointersToOtherTSL(self, PointersToOtherTSL):
        self.PointersToOtherTSL = PointersToOtherTSL
    def get_ListIssueDateTime(self):
        return self.ListIssueDateTime
    def set_ListIssueDateTime(self, ListIssueDateTime):
        self.ListIssueDateTime = ListIssueDateTime
    def get_NextUpdate(self):
        return self.NextUpdate
    def set_NextUpdate(self, NextUpdate):
        self.NextUpdate = NextUpdate
    def get_DistributionPoints(self):
        return self.DistributionPoints
    def set_DistributionPoints(self, DistributionPoints):
        self.DistributionPoints = DistributionPoints
    def get_SchemeExtensions(self):
        return self.SchemeExtensions
    def set_SchemeExtensions(self, SchemeExtensions):
        self.SchemeExtensions = SchemeExtensions
    def has__content(self):
        if (
            self.TSLVersionIdentifier is not None or
            self.TSLSequenceNumber is not None or
            self.TSLType is not None or
            self.SchemeOperatorName is not None or
            self.SchemeOperatorAddress is not None or
            self.SchemeName is not None or
            self.SchemeInformationURI is not None or
            self.StatusDeterminationApproach is not None or
            self.SchemeTypeCommunityRules is not None or
            self.SchemeTerritory is not None or
            self.PolicyOrLegalNotice is not None or
            self.HistoricalInformationPeriod is not None or
            self.PointersToOtherTSL is not None or
            self.ListIssueDateTime is not None or
            self.NextUpdate is not None or
            self.DistributionPoints is not None or
            self.SchemeExtensions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TSLSchemeInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSLSchemeInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSLSchemeInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSLSchemeInformationType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSLSchemeInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSLSchemeInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TSLSchemeInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TSLVersionIdentifier is not None:
            namespaceprefix_ = self.TSLVersionIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.TSLVersionIdentifier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTSLVersionIdentifier>%s</%sTSLVersionIdentifier>%s' % (namespaceprefix_ , self.gds_format_integer(self.TSLVersionIdentifier, input_name='TSLVersionIdentifier'), namespaceprefix_ , eol_))
        if self.TSLSequenceNumber is not None:
            namespaceprefix_ = self.TSLSequenceNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.TSLSequenceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTSLSequenceNumber>%s</%sTSLSequenceNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.TSLSequenceNumber, input_name='TSLSequenceNumber'), namespaceprefix_ , eol_))
        if self.TSLType is not None:
            namespaceprefix_ = self.TSLType_nsprefix_ + ':' if (UseCapturedNS_ and self.TSLType_nsprefix_) else ''
            self.TSLType.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='TSLType', pretty_print=pretty_print)
        if self.SchemeOperatorName is not None:
            namespaceprefix_ = self.SchemeOperatorName_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeOperatorName_nsprefix_) else ''
            self.SchemeOperatorName.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='SchemeOperatorName', pretty_print=pretty_print)
        if self.SchemeOperatorAddress is not None:
            namespaceprefix_ = self.SchemeOperatorAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeOperatorAddress_nsprefix_) else ''
            self.SchemeOperatorAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SchemeOperatorAddress', pretty_print=pretty_print)
        if self.SchemeName is not None:
            namespaceprefix_ = self.SchemeName_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeName_nsprefix_) else ''
            self.SchemeName.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='SchemeName', pretty_print=pretty_print)
        if self.SchemeInformationURI is not None:
            namespaceprefix_ = self.SchemeInformationURI_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeInformationURI_nsprefix_) else ''
            self.SchemeInformationURI.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='SchemeInformationURI', pretty_print=pretty_print)
        if self.StatusDeterminationApproach is not None:
            namespaceprefix_ = self.StatusDeterminationApproach_nsprefix_ + ':' if (UseCapturedNS_ and self.StatusDeterminationApproach_nsprefix_) else ''
            self.StatusDeterminationApproach.export(outfile, level, namespaceprefix_, namespacedef_='', name_='StatusDeterminationApproach', pretty_print=pretty_print)
        if self.SchemeTypeCommunityRules is not None:
            namespaceprefix_ = self.SchemeTypeCommunityRules_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeTypeCommunityRules_nsprefix_) else ''
            self.SchemeTypeCommunityRules.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='SchemeTypeCommunityRules', pretty_print=pretty_print)
        if self.SchemeTerritory is not None:
            namespaceprefix_ = self.SchemeTerritory_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeTerritory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSchemeTerritory>%s</%sSchemeTerritory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SchemeTerritory), input_name='SchemeTerritory')), namespaceprefix_ , eol_))
        if self.PolicyOrLegalNotice is not None:
            namespaceprefix_ = self.PolicyOrLegalNotice_nsprefix_ + ':' if (UseCapturedNS_ and self.PolicyOrLegalNotice_nsprefix_) else ''
            self.PolicyOrLegalNotice.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='PolicyOrLegalNotice', pretty_print=pretty_print)
        if self.HistoricalInformationPeriod is not None:
            namespaceprefix_ = self.HistoricalInformationPeriod_nsprefix_ + ':' if (UseCapturedNS_ and self.HistoricalInformationPeriod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHistoricalInformationPeriod>%s</%sHistoricalInformationPeriod>%s' % (namespaceprefix_ , self.gds_format_integer(self.HistoricalInformationPeriod, input_name='HistoricalInformationPeriod'), namespaceprefix_ , eol_))
        if self.PointersToOtherTSL is not None:
            namespaceprefix_ = self.PointersToOtherTSL_nsprefix_ + ':' if (UseCapturedNS_ and self.PointersToOtherTSL_nsprefix_) else ''
            self.PointersToOtherTSL.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='PointersToOtherTSL', pretty_print=pretty_print)
        if self.ListIssueDateTime is not None:
            namespaceprefix_ = self.ListIssueDateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.ListIssueDateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sListIssueDateTime>%s</%sListIssueDateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.ListIssueDateTime, input_name='ListIssueDateTime'), namespaceprefix_ , eol_))
        if self.NextUpdate is not None:
            namespaceprefix_ = self.NextUpdate_nsprefix_ + ':' if (UseCapturedNS_ and self.NextUpdate_nsprefix_) else ''
            self.NextUpdate.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='NextUpdate', pretty_print=pretty_print)
        if self.DistributionPoints is not None:
            namespaceprefix_ = self.DistributionPoints_nsprefix_ + ':' if (UseCapturedNS_ and self.DistributionPoints_nsprefix_) else ''
            self.DistributionPoints.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='DistributionPoints', pretty_print=pretty_print)
        if self.SchemeExtensions is not None:
            namespaceprefix_ = self.SchemeExtensions_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeExtensions_nsprefix_) else ''
            self.SchemeExtensions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SchemeExtensions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TSLVersionIdentifier' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'TSLVersionIdentifier')
            ival_ = self.gds_validate_integer(ival_, node, 'TSLVersionIdentifier')
            self.TSLVersionIdentifier = ival_
            self.TSLVersionIdentifier_nsprefix_ = child_.prefix
        elif nodeName_ == 'TSLSequenceNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'TSLSequenceNumber')
            if ival_ <= 0:
                raise_parse_error(child_, 'requires positiveInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'TSLSequenceNumber')
            self.TSLSequenceNumber = ival_
            self.TSLSequenceNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'TSLType':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSLType = obj_
            obj_.original_tagname_ = 'TSLType'
        elif nodeName_ == 'SchemeOperatorName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeOperatorName = obj_
            obj_.original_tagname_ = 'SchemeOperatorName'
        elif nodeName_ == 'SchemeOperatorAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeOperatorAddress = obj_
            obj_.original_tagname_ = 'SchemeOperatorAddress'
        elif nodeName_ == 'SchemeName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeName = obj_
            obj_.original_tagname_ = 'SchemeName'
        elif nodeName_ == 'SchemeInformationURI':
            obj_ = NonEmptyMultiLangURIListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeInformationURI = obj_
            obj_.original_tagname_ = 'SchemeInformationURI'
        elif nodeName_ == 'StatusDeterminationApproach':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.StatusDeterminationApproach = obj_
            obj_.original_tagname_ = 'StatusDeterminationApproach'
        elif nodeName_ == 'SchemeTypeCommunityRules':
            obj_ = NonEmptyMultiLangURIListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeTypeCommunityRules = obj_
            obj_.original_tagname_ = 'SchemeTypeCommunityRules'
        elif nodeName_ == 'SchemeTerritory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SchemeTerritory')
            value_ = self.gds_validate_string(value_, node, 'SchemeTerritory')
            self.SchemeTerritory = value_
            self.SchemeTerritory_nsprefix_ = child_.prefix
        elif nodeName_ == 'PolicyOrLegalNotice':
            obj_ = PolicyOrLegalnoticeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PolicyOrLegalNotice = obj_
            obj_.original_tagname_ = 'PolicyOrLegalNotice'
        elif nodeName_ == 'HistoricalInformationPeriod' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'HistoricalInformationPeriod')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'HistoricalInformationPeriod')
            self.HistoricalInformationPeriod = ival_
            self.HistoricalInformationPeriod_nsprefix_ = child_.prefix
        elif nodeName_ == 'PointersToOtherTSL':
            obj_ = OtherTSLPointersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PointersToOtherTSL = obj_
            obj_.original_tagname_ = 'PointersToOtherTSL'
        elif nodeName_ == 'ListIssueDateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.ListIssueDateTime = dval_
            self.ListIssueDateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'NextUpdate':
            obj_ = NextUpdateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NextUpdate = obj_
            obj_.original_tagname_ = 'NextUpdate'
        elif nodeName_ == 'DistributionPoints':
            obj_ = NonEmptyURIListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DistributionPoints = obj_
            obj_.original_tagname_ = 'DistributionPoints'
        elif nodeName_ == 'SchemeExtensions':
            obj_ = ExtensionsListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeExtensions = obj_
            obj_.original_tagname_ = 'SchemeExtensions'
# end class TSLSchemeInformationType


class PolicyOrLegalnoticeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TSLPolicy=None, TSLLegalNotice=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if TSLPolicy is None:
            self.TSLPolicy = []
        else:
            self.TSLPolicy = TSLPolicy
        self.TSLPolicy_nsprefix_ = "tsl"
        if TSLLegalNotice is None:
            self.TSLLegalNotice = []
        else:
            self.TSLLegalNotice = TSLLegalNotice
        self.TSLLegalNotice_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PolicyOrLegalnoticeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PolicyOrLegalnoticeType.subclass:
            return PolicyOrLegalnoticeType.subclass(*args_, **kwargs_)
        else:
            return PolicyOrLegalnoticeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TSLPolicy(self):
        return self.TSLPolicy
    def set_TSLPolicy(self, TSLPolicy):
        self.TSLPolicy = TSLPolicy
    def add_TSLPolicy(self, value):
        self.TSLPolicy.append(value)
    def insert_TSLPolicy_at(self, index, value):
        self.TSLPolicy.insert(index, value)
    def replace_TSLPolicy_at(self, index, value):
        self.TSLPolicy[index] = value
    def get_TSLLegalNotice(self):
        return self.TSLLegalNotice
    def set_TSLLegalNotice(self, TSLLegalNotice):
        self.TSLLegalNotice = TSLLegalNotice
    def add_TSLLegalNotice(self, value):
        self.TSLLegalNotice.append(value)
    def insert_TSLLegalNotice_at(self, index, value):
        self.TSLLegalNotice.insert(index, value)
    def replace_TSLLegalNotice_at(self, index, value):
        self.TSLLegalNotice[index] = value
    def has__content(self):
        if (
            self.TSLPolicy or
            self.TSLLegalNotice
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PolicyOrLegalnoticeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PolicyOrLegalnoticeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PolicyOrLegalnoticeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PolicyOrLegalnoticeType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PolicyOrLegalnoticeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PolicyOrLegalnoticeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PolicyOrLegalnoticeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TSLPolicy_ in self.TSLPolicy:
            namespaceprefix_ = self.TSLPolicy_nsprefix_ + ':' if (UseCapturedNS_ and self.TSLPolicy_nsprefix_) else ''
            TSLPolicy_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSLPolicy', pretty_print=pretty_print)
        for TSLLegalNotice_ in self.TSLLegalNotice:
            namespaceprefix_ = self.TSLLegalNotice_nsprefix_ + ':' if (UseCapturedNS_ and self.TSLLegalNotice_nsprefix_) else ''
            TSLLegalNotice_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSLLegalNotice', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TSLPolicy':
            obj_ = NonEmptyMultiLangURIType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSLPolicy.append(obj_)
            obj_.original_tagname_ = 'TSLPolicy'
        elif nodeName_ == 'TSLLegalNotice':
            obj_ = MultiLangStringType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSLLegalNotice.append(obj_)
            obj_.original_tagname_ = 'TSLLegalNotice'
# end class PolicyOrLegalnoticeType


class NextUpdateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, dateTime=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%SZ')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NextUpdateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NextUpdateType.subclass:
            return NextUpdateType.subclass(*args_, **kwargs_)
        else:
            return NextUpdateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def has__content(self):
        if (
            self.dateTime is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='NextUpdateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NextUpdateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NextUpdateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NextUpdateType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NextUpdateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NextUpdateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='NextUpdateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
# end class NextUpdateType


class OtherTSLPointersType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, OtherTSLPointer=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if OtherTSLPointer is None:
            self.OtherTSLPointer = []
        else:
            self.OtherTSLPointer = OtherTSLPointer
        self.OtherTSLPointer_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OtherTSLPointersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OtherTSLPointersType.subclass:
            return OtherTSLPointersType.subclass(*args_, **kwargs_)
        else:
            return OtherTSLPointersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_OtherTSLPointer(self):
        return self.OtherTSLPointer
    def set_OtherTSLPointer(self, OtherTSLPointer):
        self.OtherTSLPointer = OtherTSLPointer
    def add_OtherTSLPointer(self, value):
        self.OtherTSLPointer.append(value)
    def insert_OtherTSLPointer_at(self, index, value):
        self.OtherTSLPointer.insert(index, value)
    def replace_OtherTSLPointer_at(self, index, value):
        self.OtherTSLPointer[index] = value
    def has__content(self):
        if (
            self.OtherTSLPointer
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='OtherTSLPointersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OtherTSLPointersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OtherTSLPointersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OtherTSLPointersType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OtherTSLPointersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OtherTSLPointersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='OtherTSLPointersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for OtherTSLPointer_ in self.OtherTSLPointer:
            namespaceprefix_ = self.OtherTSLPointer_nsprefix_ + ':' if (UseCapturedNS_ and self.OtherTSLPointer_nsprefix_) else ''
            OtherTSLPointer_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='OtherTSLPointer', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OtherTSLPointer':
            obj_ = OtherTSLPointerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OtherTSLPointer.append(obj_)
            obj_.original_tagname_ = 'OtherTSLPointer'
# end class OtherTSLPointersType


class OtherTSLPointerType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceDigitalIdentities=None, TSLLocation=None, AdditionalInformation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.ServiceDigitalIdentities = ServiceDigitalIdentities
        self.ServiceDigitalIdentities_nsprefix_ = "tsl"
        self.TSLLocation = TSLLocation
        self.TSLLocation_nsprefix_ = "tsl"
        self.AdditionalInformation = AdditionalInformation
        self.AdditionalInformation_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OtherTSLPointerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OtherTSLPointerType.subclass:
            return OtherTSLPointerType.subclass(*args_, **kwargs_)
        else:
            return OtherTSLPointerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceDigitalIdentities(self):
        return self.ServiceDigitalIdentities
    def set_ServiceDigitalIdentities(self, ServiceDigitalIdentities):
        self.ServiceDigitalIdentities = ServiceDigitalIdentities
    def get_TSLLocation(self):
        return self.TSLLocation
    def set_TSLLocation(self, TSLLocation):
        self.TSLLocation = TSLLocation
    def get_AdditionalInformation(self):
        return self.AdditionalInformation
    def set_AdditionalInformation(self, AdditionalInformation):
        self.AdditionalInformation = AdditionalInformation
    def has__content(self):
        if (
            self.ServiceDigitalIdentities is not None or
            self.TSLLocation is not None or
            self.AdditionalInformation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='OtherTSLPointerType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OtherTSLPointerType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OtherTSLPointerType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OtherTSLPointerType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OtherTSLPointerType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OtherTSLPointerType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='OtherTSLPointerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceDigitalIdentities is not None:
            namespaceprefix_ = self.ServiceDigitalIdentities_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceDigitalIdentities_nsprefix_) else ''
            self.ServiceDigitalIdentities.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceDigitalIdentities', pretty_print=pretty_print)
        if self.TSLLocation is not None:
            namespaceprefix_ = self.TSLLocation_nsprefix_ + ':' if (UseCapturedNS_ and self.TSLLocation_nsprefix_) else ''
            self.TSLLocation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSLLocation', pretty_print=pretty_print)
        if self.AdditionalInformation is not None:
            namespaceprefix_ = self.AdditionalInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalInformation_nsprefix_) else ''
            self.AdditionalInformation.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='AdditionalInformation', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceDigitalIdentities':
            obj_ = ServiceDigitalIdentityListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceDigitalIdentities = obj_
            obj_.original_tagname_ = 'ServiceDigitalIdentities'
        elif nodeName_ == 'TSLLocation':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSLLocation = obj_
            obj_.original_tagname_ = 'TSLLocation'
        elif nodeName_ == 'AdditionalInformation':
            obj_ = AdditionalInformationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AdditionalInformation = obj_
            obj_.original_tagname_ = 'AdditionalInformation'
# end class OtherTSLPointerType


class ServiceDigitalIdentityListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceDigitalIdentity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if ServiceDigitalIdentity is None:
            self.ServiceDigitalIdentity = []
        else:
            self.ServiceDigitalIdentity = ServiceDigitalIdentity
        self.ServiceDigitalIdentity_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceDigitalIdentityListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceDigitalIdentityListType.subclass:
            return ServiceDigitalIdentityListType.subclass(*args_, **kwargs_)
        else:
            return ServiceDigitalIdentityListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceDigitalIdentity(self):
        return self.ServiceDigitalIdentity
    def set_ServiceDigitalIdentity(self, ServiceDigitalIdentity):
        self.ServiceDigitalIdentity = ServiceDigitalIdentity
    def add_ServiceDigitalIdentity(self, value):
        self.ServiceDigitalIdentity.append(value)
    def insert_ServiceDigitalIdentity_at(self, index, value):
        self.ServiceDigitalIdentity.insert(index, value)
    def replace_ServiceDigitalIdentity_at(self, index, value):
        self.ServiceDigitalIdentity[index] = value
    def has__content(self):
        if (
            self.ServiceDigitalIdentity
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ServiceDigitalIdentityListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceDigitalIdentityListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceDigitalIdentityListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDigitalIdentityListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceDigitalIdentityListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceDigitalIdentityListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ServiceDigitalIdentityListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ServiceDigitalIdentity_ in self.ServiceDigitalIdentity:
            namespaceprefix_ = self.ServiceDigitalIdentity_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceDigitalIdentity_nsprefix_) else ''
            ServiceDigitalIdentity_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceDigitalIdentity', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceDigitalIdentity':
            obj_ = DigitalIdentityListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceDigitalIdentity.append(obj_)
            obj_.original_tagname_ = 'ServiceDigitalIdentity'
# end class ServiceDigitalIdentityListType


class AdditionalInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TextualInformation=None, OtherInformation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if TextualInformation is None:
            self.TextualInformation = []
        else:
            self.TextualInformation = TextualInformation
        self.TextualInformation_nsprefix_ = "tsl"
        if OtherInformation is None:
            self.OtherInformation = []
        else:
            self.OtherInformation = OtherInformation
        self.OtherInformation_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdditionalInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdditionalInformationType.subclass:
            return AdditionalInformationType.subclass(*args_, **kwargs_)
        else:
            return AdditionalInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TextualInformation(self):
        return self.TextualInformation
    def set_TextualInformation(self, TextualInformation):
        self.TextualInformation = TextualInformation
    def add_TextualInformation(self, value):
        self.TextualInformation.append(value)
    def insert_TextualInformation_at(self, index, value):
        self.TextualInformation.insert(index, value)
    def replace_TextualInformation_at(self, index, value):
        self.TextualInformation[index] = value
    def get_OtherInformation(self):
        return self.OtherInformation
    def set_OtherInformation(self, OtherInformation):
        self.OtherInformation = OtherInformation
    def add_OtherInformation(self, value):
        self.OtherInformation.append(value)
    def insert_OtherInformation_at(self, index, value):
        self.OtherInformation.insert(index, value)
    def replace_OtherInformation_at(self, index, value):
        self.OtherInformation[index] = value
    def has__content(self):
        if (
            self.TextualInformation or
            self.OtherInformation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='AdditionalInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdditionalInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdditionalInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdditionalInformationType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdditionalInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdditionalInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='AdditionalInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TextualInformation_ in self.TextualInformation:
            namespaceprefix_ = self.TextualInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.TextualInformation_nsprefix_) else ''
            TextualInformation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextualInformation', pretty_print=pretty_print)
        for OtherInformation_ in self.OtherInformation:
            namespaceprefix_ = self.OtherInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.OtherInformation_nsprefix_) else ''
            OtherInformation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OtherInformation', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TextualInformation':
            obj_ = MultiLangStringType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextualInformation.append(obj_)
            obj_.original_tagname_ = 'TextualInformation'
        elif nodeName_ == 'OtherInformation':
            class_obj_ = self.get_class_obj_(child_, AnyType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OtherInformation.append(obj_)
            obj_.original_tagname_ = 'OtherInformation'
# end class AdditionalInformationType


class TSPType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TSPInformation=None, TSPServices=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.TSPInformation = TSPInformation
        self.TSPInformation_nsprefix_ = "tsl"
        self.TSPServices = TSPServices
        self.TSPServices_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSPType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSPType.subclass:
            return TSPType.subclass(*args_, **kwargs_)
        else:
            return TSPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TSPInformation(self):
        return self.TSPInformation
    def set_TSPInformation(self, TSPInformation):
        self.TSPInformation = TSPInformation
    def get_TSPServices(self):
        return self.TSPServices
    def set_TSPServices(self, TSPServices):
        self.TSPServices = TSPServices
    def has__content(self):
        if (
            self.TSPInformation is not None or
            self.TSPServices is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSPType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSPType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSPType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSPType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSPType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TSPInformation is not None:
            namespaceprefix_ = self.TSPInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPInformation_nsprefix_) else ''
            self.TSPInformation.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='TSPInformation', pretty_print=pretty_print)
        if self.TSPServices is not None:
            namespaceprefix_ = self.TSPServices_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPServices_nsprefix_) else ''
            self.TSPServices.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='TSPServices', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TSPInformation':
            obj_ = TSPInformationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPInformation = obj_
            obj_.original_tagname_ = 'TSPInformation'
        elif nodeName_ == 'TSPServices':
            obj_ = TSPServicesListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPServices = obj_
            obj_.original_tagname_ = 'TSPServices'
# end class TSPType


class TSPInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TSPName=None, TSPTradeName=None, TSPAddress=None, TSPInformationURI=None, TSPInformationExtensions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.TSPName = TSPName
        self.TSPName_nsprefix_ = "tsl"
        self.TSPTradeName = TSPTradeName
        self.TSPTradeName_nsprefix_ = "tsl"
        self.TSPAddress = TSPAddress
        self.TSPAddress_nsprefix_ = "tsl"
        self.TSPInformationURI = TSPInformationURI
        self.TSPInformationURI_nsprefix_ = "tsl"
        self.TSPInformationExtensions = TSPInformationExtensions
        self.TSPInformationExtensions_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSPInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSPInformationType.subclass:
            return TSPInformationType.subclass(*args_, **kwargs_)
        else:
            return TSPInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TSPName(self):
        return self.TSPName
    def set_TSPName(self, TSPName):
        self.TSPName = TSPName
    def get_TSPTradeName(self):
        return self.TSPTradeName
    def set_TSPTradeName(self, TSPTradeName):
        self.TSPTradeName = TSPTradeName
    def get_TSPAddress(self):
        return self.TSPAddress
    def set_TSPAddress(self, TSPAddress):
        self.TSPAddress = TSPAddress
    def get_TSPInformationURI(self):
        return self.TSPInformationURI
    def set_TSPInformationURI(self, TSPInformationURI):
        self.TSPInformationURI = TSPInformationURI
    def get_TSPInformationExtensions(self):
        return self.TSPInformationExtensions
    def set_TSPInformationExtensions(self, TSPInformationExtensions):
        self.TSPInformationExtensions = TSPInformationExtensions
    def has__content(self):
        if (
            self.TSPName is not None or
            self.TSPTradeName is not None or
            self.TSPAddress is not None or
            self.TSPInformationURI is not None or
            self.TSPInformationExtensions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSPInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSPInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSPInformationType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSPInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSPInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TSPName is not None:
            namespaceprefix_ = self.TSPName_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPName_nsprefix_) else ''
            self.TSPName.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPName', pretty_print=pretty_print)
        if self.TSPTradeName is not None:
            namespaceprefix_ = self.TSPTradeName_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPTradeName_nsprefix_) else ''
            self.TSPTradeName.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPTradeName', pretty_print=pretty_print)
        if self.TSPAddress is not None:
            namespaceprefix_ = self.TSPAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPAddress_nsprefix_) else ''
            self.TSPAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPAddress', pretty_print=pretty_print)
        if self.TSPInformationURI is not None:
            namespaceprefix_ = self.TSPInformationURI_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPInformationURI_nsprefix_) else ''
            self.TSPInformationURI.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPInformationURI', pretty_print=pretty_print)
        if self.TSPInformationExtensions is not None:
            namespaceprefix_ = self.TSPInformationExtensions_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPInformationExtensions_nsprefix_) else ''
            self.TSPInformationExtensions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPInformationExtensions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TSPName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPName = obj_
            obj_.original_tagname_ = 'TSPName'
        elif nodeName_ == 'TSPTradeName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPTradeName = obj_
            obj_.original_tagname_ = 'TSPTradeName'
        elif nodeName_ == 'TSPAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPAddress = obj_
            obj_.original_tagname_ = 'TSPAddress'
        elif nodeName_ == 'TSPInformationURI':
            obj_ = NonEmptyMultiLangURIListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPInformationURI = obj_
            obj_.original_tagname_ = 'TSPInformationURI'
        elif nodeName_ == 'TSPInformationExtensions':
            obj_ = ExtensionsListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPInformationExtensions = obj_
            obj_.original_tagname_ = 'TSPInformationExtensions'
# end class TSPInformationType


class TSPServicesListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TSPService=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if TSPService is None:
            self.TSPService = []
        else:
            self.TSPService = TSPService
        self.TSPService_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSPServicesListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSPServicesListType.subclass:
            return TSPServicesListType.subclass(*args_, **kwargs_)
        else:
            return TSPServicesListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TSPService(self):
        return self.TSPService
    def set_TSPService(self, TSPService):
        self.TSPService = TSPService
    def add_TSPService(self, value):
        self.TSPService.append(value)
    def insert_TSPService_at(self, index, value):
        self.TSPService.insert(index, value)
    def replace_TSPService_at(self, index, value):
        self.TSPService[index] = value
    def has__content(self):
        if (
            self.TSPService
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPServicesListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSPServicesListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSPServicesListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSPServicesListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSPServicesListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSPServicesListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPServicesListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TSPService_ in self.TSPService:
            namespaceprefix_ = self.TSPService_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPService_nsprefix_) else ''
            TSPService_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='TSPService', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TSPService':
            obj_ = TSPServiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPService.append(obj_)
            obj_.original_tagname_ = 'TSPService'
# end class TSPServicesListType


class TSPServiceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceInformation=None, ServiceHistory=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.ServiceInformation = ServiceInformation
        self.ServiceInformation_nsprefix_ = "tsl"
        self.ServiceHistory = ServiceHistory
        self.ServiceHistory_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSPServiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSPServiceType.subclass:
            return TSPServiceType.subclass(*args_, **kwargs_)
        else:
            return TSPServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceInformation(self):
        return self.ServiceInformation
    def set_ServiceInformation(self, ServiceInformation):
        self.ServiceInformation = ServiceInformation
    def get_ServiceHistory(self):
        return self.ServiceHistory
    def set_ServiceHistory(self, ServiceHistory):
        self.ServiceHistory = ServiceHistory
    def has__content(self):
        if (
            self.ServiceInformation is not None or
            self.ServiceHistory is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPServiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSPServiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSPServiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSPServiceType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSPServiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSPServiceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TSPServiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceInformation is not None:
            namespaceprefix_ = self.ServiceInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceInformation_nsprefix_) else ''
            self.ServiceInformation.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceInformation', pretty_print=pretty_print)
        if self.ServiceHistory is not None:
            namespaceprefix_ = self.ServiceHistory_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceHistory_nsprefix_) else ''
            self.ServiceHistory.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceHistory', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceInformation':
            obj_ = TSPServiceInformationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceInformation = obj_
            obj_.original_tagname_ = 'ServiceInformation'
        elif nodeName_ == 'ServiceHistory':
            obj_ = ServiceHistoryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceHistory = obj_
            obj_.original_tagname_ = 'ServiceHistory'
# end class TSPServiceType


class TSPServiceInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceTypeIdentifier=None, ServiceName=None, ServiceDigitalIdentity=None, ServiceStatus=None, StatusStartingTime=None, SchemeServiceDefinitionURI=None, ServiceSupplyPoints=None, TSPServiceDefinitionURI=None, ServiceInformationExtensions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ServiceTypeIdentifier = ServiceTypeIdentifier
        self.ServiceTypeIdentifier_nsprefix_ = "tsl"
        self.ServiceName = ServiceName
        self.ServiceName_nsprefix_ = "tsl"
        self.ServiceDigitalIdentity = ServiceDigitalIdentity
        self.ServiceDigitalIdentity_nsprefix_ = "tsl"
        self.ServiceStatus = ServiceStatus
        self.ServiceStatus_nsprefix_ = "tsl"
        if isinstance(StatusStartingTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(StatusStartingTime, '%Y-%m-%dT%H:%M:%SZ')
        else:
            initvalue_ = StatusStartingTime
        self.StatusStartingTime = initvalue_
        self.StatusStartingTime_nsprefix_ = None
        self.SchemeServiceDefinitionURI = SchemeServiceDefinitionURI
        self.SchemeServiceDefinitionURI_nsprefix_ = "tsl"
        self.ServiceSupplyPoints = ServiceSupplyPoints
        self.ServiceSupplyPoints_nsprefix_ = "tsl"
        self.TSPServiceDefinitionURI = TSPServiceDefinitionURI
        self.TSPServiceDefinitionURI_nsprefix_ = "tsl"
        self.ServiceInformationExtensions = ServiceInformationExtensions
        self.ServiceInformationExtensions_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSPServiceInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSPServiceInformationType.subclass:
            return TSPServiceInformationType.subclass(*args_, **kwargs_)
        else:
            return TSPServiceInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceTypeIdentifier(self):
        return self.ServiceTypeIdentifier
    def set_ServiceTypeIdentifier(self, ServiceTypeIdentifier):
        self.ServiceTypeIdentifier = ServiceTypeIdentifier
    def get_ServiceName(self):
        return self.ServiceName
    def set_ServiceName(self, ServiceName):
        self.ServiceName = ServiceName
    def get_ServiceDigitalIdentity(self):
        return self.ServiceDigitalIdentity
    def set_ServiceDigitalIdentity(self, ServiceDigitalIdentity):
        self.ServiceDigitalIdentity = ServiceDigitalIdentity
    def get_ServiceStatus(self):
        return self.ServiceStatus
    def set_ServiceStatus(self, ServiceStatus):
        self.ServiceStatus = ServiceStatus
    def get_StatusStartingTime(self):
        return self.StatusStartingTime
    def set_StatusStartingTime(self, StatusStartingTime):
        self.StatusStartingTime = StatusStartingTime
    def get_SchemeServiceDefinitionURI(self):
        return self.SchemeServiceDefinitionURI
    def set_SchemeServiceDefinitionURI(self, SchemeServiceDefinitionURI):
        self.SchemeServiceDefinitionURI = SchemeServiceDefinitionURI
    def get_ServiceSupplyPoints(self):
        return self.ServiceSupplyPoints
    def set_ServiceSupplyPoints(self, ServiceSupplyPoints):
        self.ServiceSupplyPoints = ServiceSupplyPoints
    def get_TSPServiceDefinitionURI(self):
        return self.TSPServiceDefinitionURI
    def set_TSPServiceDefinitionURI(self, TSPServiceDefinitionURI):
        self.TSPServiceDefinitionURI = TSPServiceDefinitionURI
    def get_ServiceInformationExtensions(self):
        return self.ServiceInformationExtensions
    def set_ServiceInformationExtensions(self, ServiceInformationExtensions):
        self.ServiceInformationExtensions = ServiceInformationExtensions
    def has__content(self):
        if (
            self.ServiceTypeIdentifier is not None or
            self.ServiceName is not None or
            self.ServiceDigitalIdentity is not None or
            self.ServiceStatus is not None or
            self.StatusStartingTime is not None or
            self.SchemeServiceDefinitionURI is not None or
            self.ServiceSupplyPoints is not None or
            self.TSPServiceDefinitionURI is not None or
            self.ServiceInformationExtensions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TSPServiceInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSPServiceInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSPServiceInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSPServiceInformationType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSPServiceInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSPServiceInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TSPServiceInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceTypeIdentifier is not None:
            namespaceprefix_ = self.ServiceTypeIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceTypeIdentifier_nsprefix_) else ''
            self.ServiceTypeIdentifier.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceTypeIdentifier', pretty_print=pretty_print)
        if self.ServiceName is not None:
            namespaceprefix_ = self.ServiceName_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceName_nsprefix_) else ''
            self.ServiceName.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceName', pretty_print=pretty_print)
        if self.ServiceDigitalIdentity is not None:
            namespaceprefix_ = self.ServiceDigitalIdentity_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceDigitalIdentity_nsprefix_) else ''
            self.ServiceDigitalIdentity.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceDigitalIdentity', pretty_print=pretty_print)
        if self.ServiceStatus is not None:
            namespaceprefix_ = self.ServiceStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceStatus_nsprefix_) else ''
            self.ServiceStatus.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceStatus', pretty_print=pretty_print)
        if self.StatusStartingTime is not None:
            namespaceprefix_ = self.StatusStartingTime_nsprefix_ + ':' if (UseCapturedNS_ and self.StatusStartingTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatusStartingTime>%s</%sStatusStartingTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.StatusStartingTime, input_name='StatusStartingTime'), namespaceprefix_ , eol_))
        if self.SchemeServiceDefinitionURI is not None:
            namespaceprefix_ = self.SchemeServiceDefinitionURI_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeServiceDefinitionURI_nsprefix_) else ''
            self.SchemeServiceDefinitionURI.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SchemeServiceDefinitionURI', pretty_print=pretty_print)
        if self.ServiceSupplyPoints is not None:
            namespaceprefix_ = self.ServiceSupplyPoints_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceSupplyPoints_nsprefix_) else ''
            self.ServiceSupplyPoints.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceSupplyPoints', pretty_print=pretty_print)
        if self.TSPServiceDefinitionURI is not None:
            namespaceprefix_ = self.TSPServiceDefinitionURI_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPServiceDefinitionURI_nsprefix_) else ''
            self.TSPServiceDefinitionURI.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPServiceDefinitionURI', pretty_print=pretty_print)
        if self.ServiceInformationExtensions is not None:
            namespaceprefix_ = self.ServiceInformationExtensions_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceInformationExtensions_nsprefix_) else ''
            self.ServiceInformationExtensions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceInformationExtensions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceTypeIdentifier':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceTypeIdentifier = obj_
            obj_.original_tagname_ = 'ServiceTypeIdentifier'
        elif nodeName_ == 'ServiceName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceName = obj_
            obj_.original_tagname_ = 'ServiceName'
        elif nodeName_ == 'ServiceDigitalIdentity':
            obj_ = DigitalIdentityListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceDigitalIdentity = obj_
            obj_.original_tagname_ = 'ServiceDigitalIdentity'
        elif nodeName_ == 'ServiceStatus':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceStatus = obj_
            obj_.original_tagname_ = 'ServiceStatus'
        elif nodeName_ == 'StatusStartingTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.StatusStartingTime = dval_
            self.StatusStartingTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'SchemeServiceDefinitionURI':
            obj_ = NonEmptyMultiLangURIListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeServiceDefinitionURI = obj_
            obj_.original_tagname_ = 'SchemeServiceDefinitionURI'
        elif nodeName_ == 'ServiceSupplyPoints':
            obj_ = ServiceSupplyPointsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceSupplyPoints = obj_
            obj_.original_tagname_ = 'ServiceSupplyPoints'
        elif nodeName_ == 'TSPServiceDefinitionURI':
            obj_ = NonEmptyMultiLangURIListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPServiceDefinitionURI = obj_
            obj_.original_tagname_ = 'TSPServiceDefinitionURI'
        elif nodeName_ == 'ServiceInformationExtensions':
            obj_ = ExtensionsListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceInformationExtensions = obj_
            obj_.original_tagname_ = 'ServiceInformationExtensions'
# end class TSPServiceInformationType


class ServiceSupplyPointsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceSupplyPoint=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if ServiceSupplyPoint is None:
            self.ServiceSupplyPoint = []
        else:
            self.ServiceSupplyPoint = ServiceSupplyPoint
        self.ServiceSupplyPoint_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceSupplyPointsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceSupplyPointsType.subclass:
            return ServiceSupplyPointsType.subclass(*args_, **kwargs_)
        else:
            return ServiceSupplyPointsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceSupplyPoint(self):
        return self.ServiceSupplyPoint
    def set_ServiceSupplyPoint(self, ServiceSupplyPoint):
        self.ServiceSupplyPoint = ServiceSupplyPoint
    def add_ServiceSupplyPoint(self, value):
        self.ServiceSupplyPoint.append(value)
    def insert_ServiceSupplyPoint_at(self, index, value):
        self.ServiceSupplyPoint.insert(index, value)
    def replace_ServiceSupplyPoint_at(self, index, value):
        self.ServiceSupplyPoint[index] = value
    def has__content(self):
        if (
            self.ServiceSupplyPoint
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ServiceSupplyPointsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceSupplyPointsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceSupplyPointsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceSupplyPointsType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceSupplyPointsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceSupplyPointsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ServiceSupplyPointsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ServiceSupplyPoint_ in self.ServiceSupplyPoint:
            namespaceprefix_ = self.ServiceSupplyPoint_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceSupplyPoint_nsprefix_) else ''
            ServiceSupplyPoint_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceSupplyPoint', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceSupplyPoint':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceSupplyPoint.append(obj_)
            obj_.original_tagname_ = 'ServiceSupplyPoint'
# end class ServiceSupplyPointsType


class DigitalIdentityListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, DigitalId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if DigitalId is None:
            self.DigitalId = []
        else:
            self.DigitalId = DigitalId
        self.DigitalId_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigitalIdentityListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigitalIdentityListType.subclass:
            return DigitalIdentityListType.subclass(*args_, **kwargs_)
        else:
            return DigitalIdentityListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DigitalId(self):
        return self.DigitalId
    def set_DigitalId(self, DigitalId):
        self.DigitalId = DigitalId
    def add_DigitalId(self, value):
        self.DigitalId.append(value)
    def insert_DigitalId_at(self, index, value):
        self.DigitalId.insert(index, value)
    def replace_DigitalId_at(self, index, value):
        self.DigitalId[index] = value
    def has__content(self):
        if (
            self.DigitalId
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='DigitalIdentityListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigitalIdentityListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigitalIdentityListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigitalIdentityListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigitalIdentityListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigitalIdentityListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='DigitalIdentityListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for DigitalId_ in self.DigitalId:
            namespaceprefix_ = self.DigitalId_nsprefix_ + ':' if (UseCapturedNS_ and self.DigitalId_nsprefix_) else ''
            DigitalId_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DigitalId', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DigitalId':
            obj_ = DigitalIdentityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigitalId.append(obj_)
            obj_.original_tagname_ = 'DigitalId'
# end class DigitalIdentityListType


class DigitalIdentityType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, X509Certificate=None, X509SubjectName=None, KeyValue=None, X509SKI=None, Other=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.X509Certificate = X509Certificate
        self.X509Certificate_nsprefix_ = None
        self.X509SubjectName = X509SubjectName
        self.X509SubjectName_nsprefix_ = None
        self.KeyValue = KeyValue
        self.KeyValue_nsprefix_ = "ds"
        self.X509SKI = X509SKI
        self.X509SKI_nsprefix_ = None
        self.Other = Other
        self.Other_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigitalIdentityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigitalIdentityType.subclass:
            return DigitalIdentityType.subclass(*args_, **kwargs_)
        else:
            return DigitalIdentityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_X509Certificate(self):
        return self.X509Certificate
    def set_X509Certificate(self, X509Certificate):
        self.X509Certificate = X509Certificate
    def get_X509SubjectName(self):
        return self.X509SubjectName
    def set_X509SubjectName(self, X509SubjectName):
        self.X509SubjectName = X509SubjectName
    def get_KeyValue(self):
        return self.KeyValue
    def set_KeyValue(self, KeyValue):
        self.KeyValue = KeyValue
    def get_X509SKI(self):
        return self.X509SKI
    def set_X509SKI(self, X509SKI):
        self.X509SKI = X509SKI
    def get_Other(self):
        return self.Other
    def set_Other(self, Other):
        self.Other = Other
    def has__content(self):
        if (
            self.X509Certificate is not None or
            self.X509SubjectName is not None or
            self.KeyValue is not None or
            self.X509SKI is not None or
            self.Other is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='DigitalIdentityType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigitalIdentityType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigitalIdentityType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigitalIdentityType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigitalIdentityType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigitalIdentityType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='DigitalIdentityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509Certificate is not None:
            namespaceprefix_ = self.X509Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509Certificate>%s</%sX509Certificate>%s' % (namespaceprefix_ , self.gds_format_base64(self.X509Certificate, input_name='X509Certificate'), namespaceprefix_ , eol_))
        if self.X509SubjectName is not None:
            namespaceprefix_ = self.X509SubjectName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SubjectName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SubjectName>%s</%sX509SubjectName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509SubjectName), input_name='X509SubjectName')), namespaceprefix_ , eol_))
        if self.KeyValue is not None:
            namespaceprefix_ = self.KeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyValue_nsprefix_) else ''
            self.KeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValue', pretty_print=pretty_print)
        if self.X509SKI is not None:
            namespaceprefix_ = self.X509SKI_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SKI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SKI>%s</%sX509SKI>%s' % (namespaceprefix_ , self.gds_format_base64(self.X509SKI, input_name='X509SKI'), namespaceprefix_ , eol_))
        if self.Other is not None:
            namespaceprefix_ = self.Other_nsprefix_ + ':' if (UseCapturedNS_ and self.Other_nsprefix_) else ''
            self.Other.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Other', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509Certificate':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'X509Certificate')
            else:
                bval_ = None
            self.X509Certificate = bval_
            self.X509Certificate_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SubjectName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SubjectName')
            value_ = self.gds_validate_string(value_, node, 'X509SubjectName')
            self.X509SubjectName = value_
            self.X509SubjectName_nsprefix_ = child_.prefix
        elif nodeName_ == 'KeyValue':
            obj_ = KeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyValue = obj_
            obj_.original_tagname_ = 'KeyValue'
        elif nodeName_ == 'X509SKI':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'X509SKI')
            else:
                bval_ = None
            self.X509SKI = bval_
            self.X509SKI_nsprefix_ = child_.prefix
        elif nodeName_ == 'Other':
            class_obj_ = self.get_class_obj_(child_, AnyType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Other = obj_
            obj_.original_tagname_ = 'Other'
# end class DigitalIdentityType


class ServiceHistoryType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceHistoryInstance=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if ServiceHistoryInstance is None:
            self.ServiceHistoryInstance = []
        else:
            self.ServiceHistoryInstance = ServiceHistoryInstance
        self.ServiceHistoryInstance_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceHistoryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceHistoryType.subclass:
            return ServiceHistoryType.subclass(*args_, **kwargs_)
        else:
            return ServiceHistoryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceHistoryInstance(self):
        return self.ServiceHistoryInstance
    def set_ServiceHistoryInstance(self, ServiceHistoryInstance):
        self.ServiceHistoryInstance = ServiceHistoryInstance
    def add_ServiceHistoryInstance(self, value):
        self.ServiceHistoryInstance.append(value)
    def insert_ServiceHistoryInstance_at(self, index, value):
        self.ServiceHistoryInstance.insert(index, value)
    def replace_ServiceHistoryInstance_at(self, index, value):
        self.ServiceHistoryInstance[index] = value
    def has__content(self):
        if (
            self.ServiceHistoryInstance
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ServiceHistoryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceHistoryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceHistoryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceHistoryType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceHistoryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceHistoryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ServiceHistoryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ServiceHistoryInstance_ in self.ServiceHistoryInstance:
            namespaceprefix_ = self.ServiceHistoryInstance_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceHistoryInstance_nsprefix_) else ''
            ServiceHistoryInstance_.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceHistoryInstance', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceHistoryInstance':
            obj_ = ServiceHistoryInstanceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceHistoryInstance.append(obj_)
            obj_.original_tagname_ = 'ServiceHistoryInstance'
# end class ServiceHistoryType


class ServiceHistoryInstanceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceTypeIdentifier=None, ServiceName=None, ServiceDigitalIdentity=None, ServiceStatus=None, StatusStartingTime=None, ServiceInformationExtensions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ServiceTypeIdentifier = ServiceTypeIdentifier
        self.ServiceTypeIdentifier_nsprefix_ = "tsl"
        self.ServiceName = ServiceName
        self.ServiceName_nsprefix_ = "tsl"
        self.ServiceDigitalIdentity = ServiceDigitalIdentity
        self.ServiceDigitalIdentity_nsprefix_ = "tsl"
        self.ServiceStatus = ServiceStatus
        self.ServiceStatus_nsprefix_ = "tsl"
        if isinstance(StatusStartingTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(StatusStartingTime, '%Y-%m-%dT%H:%M:%SZ')
        else:
            initvalue_ = StatusStartingTime
        self.StatusStartingTime = initvalue_
        self.StatusStartingTime_nsprefix_ = None
        self.ServiceInformationExtensions = ServiceInformationExtensions
        self.ServiceInformationExtensions_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceHistoryInstanceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceHistoryInstanceType.subclass:
            return ServiceHistoryInstanceType.subclass(*args_, **kwargs_)
        else:
            return ServiceHistoryInstanceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceTypeIdentifier(self):
        return self.ServiceTypeIdentifier
    def set_ServiceTypeIdentifier(self, ServiceTypeIdentifier):
        self.ServiceTypeIdentifier = ServiceTypeIdentifier
    def get_ServiceName(self):
        return self.ServiceName
    def set_ServiceName(self, ServiceName):
        self.ServiceName = ServiceName
    def get_ServiceDigitalIdentity(self):
        return self.ServiceDigitalIdentity
    def set_ServiceDigitalIdentity(self, ServiceDigitalIdentity):
        self.ServiceDigitalIdentity = ServiceDigitalIdentity
    def get_ServiceStatus(self):
        return self.ServiceStatus
    def set_ServiceStatus(self, ServiceStatus):
        self.ServiceStatus = ServiceStatus
    def get_StatusStartingTime(self):
        return self.StatusStartingTime
    def set_StatusStartingTime(self, StatusStartingTime):
        self.StatusStartingTime = StatusStartingTime
    def get_ServiceInformationExtensions(self):
        return self.ServiceInformationExtensions
    def set_ServiceInformationExtensions(self, ServiceInformationExtensions):
        self.ServiceInformationExtensions = ServiceInformationExtensions
    def has__content(self):
        if (
            self.ServiceTypeIdentifier is not None or
            self.ServiceName is not None or
            self.ServiceDigitalIdentity is not None or
            self.ServiceStatus is not None or
            self.StatusStartingTime is not None or
            self.ServiceInformationExtensions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='ServiceHistoryInstanceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceHistoryInstanceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceHistoryInstanceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceHistoryInstanceType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceHistoryInstanceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceHistoryInstanceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='ServiceHistoryInstanceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceTypeIdentifier is not None:
            namespaceprefix_ = self.ServiceTypeIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceTypeIdentifier_nsprefix_) else ''
            self.ServiceTypeIdentifier.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceTypeIdentifier', pretty_print=pretty_print)
        if self.ServiceName is not None:
            namespaceprefix_ = self.ServiceName_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceName_nsprefix_) else ''
            self.ServiceName.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceName', pretty_print=pretty_print)
        if self.ServiceDigitalIdentity is not None:
            namespaceprefix_ = self.ServiceDigitalIdentity_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceDigitalIdentity_nsprefix_) else ''
            self.ServiceDigitalIdentity.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceDigitalIdentity', pretty_print=pretty_print)
        if self.ServiceStatus is not None:
            namespaceprefix_ = self.ServiceStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceStatus_nsprefix_) else ''
            self.ServiceStatus.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='ServiceStatus', pretty_print=pretty_print)
        if self.StatusStartingTime is not None:
            namespaceprefix_ = self.StatusStartingTime_nsprefix_ + ':' if (UseCapturedNS_ and self.StatusStartingTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatusStartingTime>%s</%sStatusStartingTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.StatusStartingTime, input_name='StatusStartingTime'), namespaceprefix_ , eol_))
        if self.ServiceInformationExtensions is not None:
            namespaceprefix_ = self.ServiceInformationExtensions_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceInformationExtensions_nsprefix_) else ''
            self.ServiceInformationExtensions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceInformationExtensions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceTypeIdentifier':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceTypeIdentifier = obj_
            obj_.original_tagname_ = 'ServiceTypeIdentifier'
        elif nodeName_ == 'ServiceName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceName = obj_
            obj_.original_tagname_ = 'ServiceName'
        elif nodeName_ == 'ServiceDigitalIdentity':
            obj_ = DigitalIdentityListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceDigitalIdentity = obj_
            obj_.original_tagname_ = 'ServiceDigitalIdentity'
        elif nodeName_ == 'ServiceStatus':
            class_obj_ = self.get_class_obj_(child_, NonEmptyURIType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceStatus = obj_
            obj_.original_tagname_ = 'ServiceStatus'
        elif nodeName_ == 'StatusStartingTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.StatusStartingTime = dval_
            self.StatusStartingTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'ServiceInformationExtensions':
            obj_ = ExtensionsListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceInformationExtensions = obj_
            obj_.original_tagname_ = 'ServiceInformationExtensions'
# end class ServiceHistoryInstanceType


class AdditionalServiceInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, InformationValue=None, OtherInformation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.URI = URI
        self.URI_nsprefix_ = "tsl"
        self.InformationValue = InformationValue
        self.InformationValue_nsprefix_ = None
        self.OtherInformation = OtherInformation
        self.OtherInformation_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdditionalServiceInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdditionalServiceInformationType.subclass:
            return AdditionalServiceInformationType.subclass(*args_, **kwargs_)
        else:
            return AdditionalServiceInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def get_InformationValue(self):
        return self.InformationValue
    def set_InformationValue(self, InformationValue):
        self.InformationValue = InformationValue
    def get_OtherInformation(self):
        return self.OtherInformation
    def set_OtherInformation(self, OtherInformation):
        self.OtherInformation = OtherInformation
    def has__content(self):
        if (
            self.URI is not None or
            self.InformationValue is not None or
            self.OtherInformation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='AdditionalServiceInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdditionalServiceInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdditionalServiceInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdditionalServiceInformationType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdditionalServiceInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdditionalServiceInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='AdditionalServiceInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.URI is not None:
            namespaceprefix_ = self.URI_nsprefix_ + ':' if (UseCapturedNS_ and self.URI_nsprefix_) else ''
            self.URI.export(outfile, level, namespaceprefix_, namespacedef_='', name_='URI', pretty_print=pretty_print)
        if self.InformationValue is not None:
            namespaceprefix_ = self.InformationValue_nsprefix_ + ':' if (UseCapturedNS_ and self.InformationValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInformationValue>%s</%sInformationValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InformationValue), input_name='InformationValue')), namespaceprefix_ , eol_))
        if self.OtherInformation is not None:
            namespaceprefix_ = self.OtherInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.OtherInformation_nsprefix_) else ''
            self.OtherInformation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OtherInformation', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'URI':
            obj_ = NonEmptyMultiLangURIType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.URI = obj_
            obj_.original_tagname_ = 'URI'
        elif nodeName_ == 'InformationValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InformationValue')
            value_ = self.gds_validate_string(value_, node, 'InformationValue')
            self.InformationValue = value_
            self.InformationValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'OtherInformation':
            class_obj_ = self.get_class_obj_(child_, AnyType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OtherInformation = obj_
            obj_.original_tagname_ = 'OtherInformation'
# end class AdditionalServiceInformationType


class QualificationsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, QualificationElement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if QualificationElement is None:
            self.QualificationElement = []
        else:
            self.QualificationElement = QualificationElement
        self.QualificationElement_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QualificationsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QualificationsType.subclass:
            return QualificationsType.subclass(*args_, **kwargs_)
        else:
            return QualificationsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_QualificationElement(self):
        return self.QualificationElement
    def set_QualificationElement(self, QualificationElement):
        self.QualificationElement = QualificationElement
    def add_QualificationElement(self, value):
        self.QualificationElement.append(value)
    def insert_QualificationElement_at(self, index, value):
        self.QualificationElement.insert(index, value)
    def replace_QualificationElement_at(self, index, value):
        self.QualificationElement[index] = value
    def has__content(self):
        if (
            self.QualificationElement
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualificationsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QualificationsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QualificationsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QualificationsType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QualificationsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QualificationsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualificationsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for QualificationElement_ in self.QualificationElement:
            namespaceprefix_ = self.QualificationElement_nsprefix_ + ':' if (UseCapturedNS_ and self.QualificationElement_nsprefix_) else ''
            QualificationElement_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='QualificationElement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'QualificationElement':
            obj_ = QualificationElementType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.QualificationElement.append(obj_)
            obj_.original_tagname_ = 'QualificationElement'
# end class QualificationsType


class QualificationElementType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Qualifiers=None, CriteriaList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.Qualifiers = Qualifiers
        self.Qualifiers_nsprefix_ = "tsl"
        self.CriteriaList = CriteriaList
        self.CriteriaList_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QualificationElementType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QualificationElementType.subclass:
            return QualificationElementType.subclass(*args_, **kwargs_)
        else:
            return QualificationElementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Qualifiers(self):
        return self.Qualifiers
    def set_Qualifiers(self, Qualifiers):
        self.Qualifiers = Qualifiers
    def get_CriteriaList(self):
        return self.CriteriaList
    def set_CriteriaList(self, CriteriaList):
        self.CriteriaList = CriteriaList
    def has__content(self):
        if (
            self.Qualifiers is not None or
            self.CriteriaList is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualificationElementType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QualificationElementType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QualificationElementType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QualificationElementType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QualificationElementType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QualificationElementType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualificationElementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Qualifiers is not None:
            namespaceprefix_ = self.Qualifiers_nsprefix_ + ':' if (UseCapturedNS_ and self.Qualifiers_nsprefix_) else ''
            self.Qualifiers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Qualifiers', pretty_print=pretty_print)
        if self.CriteriaList is not None:
            namespaceprefix_ = self.CriteriaList_nsprefix_ + ':' if (UseCapturedNS_ and self.CriteriaList_nsprefix_) else ''
            self.CriteriaList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriteriaList', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Qualifiers':
            obj_ = QualifiersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Qualifiers = obj_
            obj_.original_tagname_ = 'Qualifiers'
        elif nodeName_ == 'CriteriaList':
            obj_ = CriteriaListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriteriaList = obj_
            obj_.original_tagname_ = 'CriteriaList'
# end class QualificationElementType


class CriteriaListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, assert_=None, KeyUsage=None, PolicySet=None, CriteriaList=None, Description=None, otherCriteriaList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.assert_ = _cast(None, assert_)
        self.assert__nsprefix_ = None
        if KeyUsage is None:
            self.KeyUsage = []
        else:
            self.KeyUsage = KeyUsage
        self.KeyUsage_nsprefix_ = "tsl"
        if PolicySet is None:
            self.PolicySet = []
        else:
            self.PolicySet = PolicySet
        self.PolicySet_nsprefix_ = "tsl"
        if CriteriaList is None:
            self.CriteriaList = []
        else:
            self.CriteriaList = CriteriaList
        self.CriteriaList_nsprefix_ = "tsl"
        self.Description = Description
        self.Description_nsprefix_ = None
        self.otherCriteriaList = otherCriteriaList
        self.otherCriteriaList_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriteriaListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriteriaListType.subclass:
            return CriteriaListType.subclass(*args_, **kwargs_)
        else:
            return CriteriaListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_KeyUsage(self):
        return self.KeyUsage
    def set_KeyUsage(self, KeyUsage):
        self.KeyUsage = KeyUsage
    def add_KeyUsage(self, value):
        self.KeyUsage.append(value)
    def insert_KeyUsage_at(self, index, value):
        self.KeyUsage.insert(index, value)
    def replace_KeyUsage_at(self, index, value):
        self.KeyUsage[index] = value
    def get_PolicySet(self):
        return self.PolicySet
    def set_PolicySet(self, PolicySet):
        self.PolicySet = PolicySet
    def add_PolicySet(self, value):
        self.PolicySet.append(value)
    def insert_PolicySet_at(self, index, value):
        self.PolicySet.insert(index, value)
    def replace_PolicySet_at(self, index, value):
        self.PolicySet[index] = value
    def get_CriteriaList(self):
        return self.CriteriaList
    def set_CriteriaList(self, CriteriaList):
        self.CriteriaList = CriteriaList
    def add_CriteriaList(self, value):
        self.CriteriaList.append(value)
    def insert_CriteriaList_at(self, index, value):
        self.CriteriaList.insert(index, value)
    def replace_CriteriaList_at(self, index, value):
        self.CriteriaList[index] = value
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def get_otherCriteriaList(self):
        return self.otherCriteriaList
    def set_otherCriteriaList(self, otherCriteriaList):
        self.otherCriteriaList = otherCriteriaList
    def get_assert(self):
        return self.assert_
    def set_assert(self, assert_):
        self.assert_ = assert_
    def validate_assertType(self, value):
        # Validate type assertType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['all', 'atLeastOne', 'none']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on assertType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def has__content(self):
        if (
            self.KeyUsage or
            self.PolicySet or
            self.CriteriaList or
            self.Description is not None or
            self.otherCriteriaList is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='CriteriaListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriteriaListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriteriaListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriteriaListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CriteriaListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriteriaListType'):
        if self.assert_ is not None and 'assert_' not in already_processed:
            already_processed.add('assert_')
            outfile.write(' assert=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.assert_), input_name='assert')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='CriteriaListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for KeyUsage_ in self.KeyUsage:
            namespaceprefix_ = self.KeyUsage_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyUsage_nsprefix_) else ''
            KeyUsage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='KeyUsage', pretty_print=pretty_print)
        for PolicySet_ in self.PolicySet:
            namespaceprefix_ = self.PolicySet_nsprefix_ + ':' if (UseCapturedNS_ and self.PolicySet_nsprefix_) else ''
            PolicySet_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PolicySet', pretty_print=pretty_print)
        for CriteriaList_ in self.CriteriaList:
            namespaceprefix_ = self.CriteriaList_nsprefix_ + ':' if (UseCapturedNS_ and self.CriteriaList_nsprefix_) else ''
            CriteriaList_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriteriaList', pretty_print=pretty_print)
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
        if self.otherCriteriaList is not None:
            namespaceprefix_ = self.otherCriteriaList_nsprefix_ + ':' if (UseCapturedNS_ and self.otherCriteriaList_nsprefix_) else ''
            self.otherCriteriaList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='otherCriteriaList', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('assert', node)
        if value is not None and 'assert' not in already_processed:
            already_processed.add('assert')
            self.assert_ = value
            self.validate_assertType(self.assert_)    # validate type assertType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KeyUsage':
            obj_ = KeyUsageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyUsage.append(obj_)
            obj_.original_tagname_ = 'KeyUsage'
        elif nodeName_ == 'PolicySet':
            obj_ = PoliciesListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PolicySet.append(obj_)
            obj_.original_tagname_ = 'PolicySet'
        elif nodeName_ == 'CriteriaList':
            obj_ = CriteriaListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriteriaList.append(obj_)
            obj_.original_tagname_ = 'CriteriaList'
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
        elif nodeName_ == 'otherCriteriaList':
            class_obj_ = self.get_class_obj_(child_, AnyType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.otherCriteriaList = obj_
            obj_.original_tagname_ = 'otherCriteriaList'
# end class CriteriaListType


class QualifiersType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Qualifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if Qualifier is None:
            self.Qualifier = []
        else:
            self.Qualifier = Qualifier
        self.Qualifier_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QualifiersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QualifiersType.subclass:
            return QualifiersType.subclass(*args_, **kwargs_)
        else:
            return QualifiersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Qualifier(self):
        return self.Qualifier
    def set_Qualifier(self, Qualifier):
        self.Qualifier = Qualifier
    def add_Qualifier(self, value):
        self.Qualifier.append(value)
    def insert_Qualifier_at(self, index, value):
        self.Qualifier.insert(index, value)
    def replace_Qualifier_at(self, index, value):
        self.Qualifier[index] = value
    def has__content(self):
        if (
            self.Qualifier
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualifiersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QualifiersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QualifiersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QualifiersType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QualifiersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QualifiersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualifiersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Qualifier_ in self.Qualifier:
            namespaceprefix_ = self.Qualifier_nsprefix_ + ':' if (UseCapturedNS_ and self.Qualifier_nsprefix_) else ''
            Qualifier_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Qualifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Qualifier':
            obj_ = QualifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Qualifier.append(obj_)
            obj_.original_tagname_ = 'Qualifier'
# end class QualifiersType


class QualifierType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, uri=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.uri = _cast(None, uri)
        self.uri_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QualifierType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QualifierType.subclass:
            return QualifierType.subclass(*args_, **kwargs_)
        else:
            return QualifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_uri(self):
        return self.uri
    def set_uri(self, uri):
        self.uri = uri
    def has__content(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualifierType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QualifierType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QualifierType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QualifierType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QualifierType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QualifierType'):
        if self.uri is not None and 'uri' not in already_processed:
            already_processed.add('uri')
            outfile.write(' uri=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.uri), input_name='uri')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='QualifierType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('uri', node)
        if value is not None and 'uri' not in already_processed:
            already_processed.add('uri')
            self.uri = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class QualifierType


class PoliciesListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PolicyIdentifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if PolicyIdentifier is None:
            self.PolicyIdentifier = []
        else:
            self.PolicyIdentifier = PolicyIdentifier
        self.PolicyIdentifier_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PoliciesListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PoliciesListType.subclass:
            return PoliciesListType.subclass(*args_, **kwargs_)
        else:
            return PoliciesListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PolicyIdentifier(self):
        return self.PolicyIdentifier
    def set_PolicyIdentifier(self, PolicyIdentifier):
        self.PolicyIdentifier = PolicyIdentifier
    def add_PolicyIdentifier(self, value):
        self.PolicyIdentifier.append(value)
    def insert_PolicyIdentifier_at(self, index, value):
        self.PolicyIdentifier.insert(index, value)
    def replace_PolicyIdentifier_at(self, index, value):
        self.PolicyIdentifier[index] = value
    def has__content(self):
        if (
            self.PolicyIdentifier
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PoliciesListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PoliciesListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PoliciesListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PoliciesListType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PoliciesListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PoliciesListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='PoliciesListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for PolicyIdentifier_ in self.PolicyIdentifier:
            namespaceprefix_ = self.PolicyIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.PolicyIdentifier_nsprefix_) else ''
            PolicyIdentifier_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PolicyIdentifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PolicyIdentifier':
            obj_ = ObjectIdentifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PolicyIdentifier.append(obj_)
            obj_.original_tagname_ = 'PolicyIdentifier'
# end class PoliciesListType


class ObjectIdentifierType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Identifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if Identifier is None:
            self.Identifier = []
        else:
            self.Identifier = Identifier
        self.Identifier_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectIdentifierType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectIdentifierType.subclass:
            return ObjectIdentifierType.subclass(*args_, **kwargs_)
        else:
            return ObjectIdentifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Identifier(self):
        return self.Identifier
    def set_Identifier(self, Identifier):
        self.Identifier = Identifier
    def add_Identifier(self, value):
        self.Identifier.append(value)
    def insert_Identifier_at(self, index, value):
        self.Identifier.insert(index, value)
    def replace_Identifier_at(self, index, value):
        self.Identifier[index] = value
    def has__content(self):
        if (
            self.Identifier
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ObjectIdentifierType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectIdentifierType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectIdentifierType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectIdentifierType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectIdentifierType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectIdentifierType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ObjectIdentifierType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Identifier_ in self.Identifier:
            namespaceprefix_ = self.Identifier_nsprefix_ + ':' if (UseCapturedNS_ and self.Identifier_nsprefix_) else ''
            Identifier_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Identifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Identifier':
            obj_ = IdentifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Identifier.append(obj_)
            obj_.original_tagname_ = 'Identifier'
# end class ObjectIdentifierType


class IdentifierType(AnyType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = AnyType
    def __init__(self, anytypeobjs_=None, Qualifier=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        super(globals().get("IdentifierType"), self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
        self.Qualifier = _cast(None, Qualifier)
        self.Qualifier_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, IdentifierType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if IdentifierType.subclass:
            return IdentifierType.subclass(*args_, **kwargs_)
        else:
            return IdentifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Qualifier(self):
        return self.Qualifier
    def set_Qualifier(self, Qualifier):
        self.Qualifier = Qualifier
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_QualifierType1(self, value):
        # Validate type QualifierType1, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OIDAsURI', 'OIDAsURN']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on QualifierType1' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_ or
            super(IdentifierType, self).has__content()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='IdentifierType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('IdentifierType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'IdentifierType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='IdentifierType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='IdentifierType'):
        super(IdentifierType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='IdentifierType')
        if self.Qualifier is not None and 'Qualifier' not in already_processed:
            already_processed.add('Qualifier')
            outfile.write(' Qualifier=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Qualifier), input_name='Qualifier')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='IdentifierType', fromsubclass_=False, pretty_print=True):
        super(IdentifierType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Qualifier', node)
        if value is not None and 'Qualifier' not in already_processed:
            already_processed.add('Qualifier')
            self.Qualifier = value
            self.validate_QualifierType1(self.Qualifier)    # validate type QualifierType1
        super(IdentifierType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(IdentifierType, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class IdentifierType


class DocumentationReferencesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, DocumentationReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if DocumentationReference is None:
            self.DocumentationReference = []
        else:
            self.DocumentationReference = DocumentationReference
        self.DocumentationReference_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DocumentationReferencesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DocumentationReferencesType.subclass:
            return DocumentationReferencesType.subclass(*args_, **kwargs_)
        else:
            return DocumentationReferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DocumentationReference(self):
        return self.DocumentationReference
    def set_DocumentationReference(self, DocumentationReference):
        self.DocumentationReference = DocumentationReference
    def add_DocumentationReference(self, value):
        self.DocumentationReference.append(value)
    def insert_DocumentationReference_at(self, index, value):
        self.DocumentationReference.insert(index, value)
    def replace_DocumentationReference_at(self, index, value):
        self.DocumentationReference[index] = value
    def has__content(self):
        if (
            self.DocumentationReference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='DocumentationReferencesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DocumentationReferencesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DocumentationReferencesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DocumentationReferencesType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DocumentationReferencesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DocumentationReferencesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='DocumentationReferencesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for DocumentationReference_ in self.DocumentationReference:
            namespaceprefix_ = self.DocumentationReference_nsprefix_ + ':' if (UseCapturedNS_ and self.DocumentationReference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDocumentationReference>%s</%sDocumentationReference>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(DocumentationReference_), input_name='DocumentationReference')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DocumentationReference':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DocumentationReference')
            value_ = self.gds_validate_string(value_, node, 'DocumentationReference')
            self.DocumentationReference.append(value_)
            self.DocumentationReference_nsprefix_ = child_.prefix
# end class DocumentationReferencesType


class KeyUsageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, KeyUsageBit=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if KeyUsageBit is None:
            self.KeyUsageBit = []
        else:
            self.KeyUsageBit = KeyUsageBit
        self.KeyUsageBit_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyUsageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyUsageType.subclass:
            return KeyUsageType.subclass(*args_, **kwargs_)
        else:
            return KeyUsageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_KeyUsageBit(self):
        return self.KeyUsageBit
    def set_KeyUsageBit(self, KeyUsageBit):
        self.KeyUsageBit = KeyUsageBit
    def add_KeyUsageBit(self, value):
        self.KeyUsageBit.append(value)
    def insert_KeyUsageBit_at(self, index, value):
        self.KeyUsageBit.insert(index, value)
    def replace_KeyUsageBit_at(self, index, value):
        self.KeyUsageBit[index] = value
    def has__content(self):
        if (
            self.KeyUsageBit
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='KeyUsageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyUsageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyUsageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyUsageType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyUsageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='KeyUsageType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='KeyUsageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for KeyUsageBit_ in self.KeyUsageBit:
            namespaceprefix_ = self.KeyUsageBit_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyUsageBit_nsprefix_) else ''
            KeyUsageBit_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='KeyUsageBit', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KeyUsageBit':
            obj_ = KeyUsageBitType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyUsageBit.append(obj_)
            obj_.original_tagname_ = 'KeyUsageBit'
# end class KeyUsageType


class KeyUsageBitType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyUsageBitType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyUsageBitType.subclass:
            return KeyUsageBitType.subclass(*args_, **kwargs_)
        else:
            return KeyUsageBitType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_nameType(self, value):
        # Validate type nameType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['digitalSignature', 'nonRepudiation', 'keyEncipherment', 'dataEncipherment', 'keyAgreement', 'keyCertSign', 'crlSign', 'encipherOnly', 'decipherOnly']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on nameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='KeyUsageBitType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyUsageBitType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyUsageBitType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyUsageBitType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='KeyUsageBitType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='KeyUsageBitType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.validate_nameType(self.name)    # validate type nameType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class KeyUsageBitType


class ExtendedKeyUsageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, KeyPurposeId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if KeyPurposeId is None:
            self.KeyPurposeId = []
        else:
            self.KeyPurposeId = KeyPurposeId
        self.KeyPurposeId_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExtendedKeyUsageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExtendedKeyUsageType.subclass:
            return ExtendedKeyUsageType.subclass(*args_, **kwargs_)
        else:
            return ExtendedKeyUsageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_KeyPurposeId(self):
        return self.KeyPurposeId
    def set_KeyPurposeId(self, KeyPurposeId):
        self.KeyPurposeId = KeyPurposeId
    def add_KeyPurposeId(self, value):
        self.KeyPurposeId.append(value)
    def insert_KeyPurposeId_at(self, index, value):
        self.KeyPurposeId.insert(index, value)
    def replace_KeyPurposeId_at(self, index, value):
        self.KeyPurposeId[index] = value
    def has__content(self):
        if (
            self.KeyPurposeId
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ExtendedKeyUsageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExtendedKeyUsageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExtendedKeyUsageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExtendedKeyUsageType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ExtendedKeyUsageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExtendedKeyUsageType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='ExtendedKeyUsageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for KeyPurposeId_ in self.KeyPurposeId:
            namespaceprefix_ = self.KeyPurposeId_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyPurposeId_nsprefix_) else ''
            KeyPurposeId_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='KeyPurposeId', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KeyPurposeId':
            obj_ = ObjectIdentifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyPurposeId.append(obj_)
            obj_.original_tagname_ = 'KeyPurposeId'
# end class ExtendedKeyUsageType


class TakenOverByType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, TSPName=None, SchemeOperatorName=None, SchemeTerritory=None, OtherQualifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.URI = URI
        self.URI_nsprefix_ = "tsl"
        self.TSPName = TSPName
        self.TSPName_nsprefix_ = "tsl"
        self.SchemeOperatorName = SchemeOperatorName
        self.SchemeOperatorName_nsprefix_ = "tsl"
        self.SchemeTerritory = SchemeTerritory
        self.SchemeTerritory_nsprefix_ = "tsl"
        if OtherQualifier is None:
            self.OtherQualifier = []
        else:
            self.OtherQualifier = OtherQualifier
        self.OtherQualifier_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TakenOverByType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TakenOverByType.subclass:
            return TakenOverByType.subclass(*args_, **kwargs_)
        else:
            return TakenOverByType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def get_TSPName(self):
        return self.TSPName
    def set_TSPName(self, TSPName):
        self.TSPName = TSPName
    def get_SchemeOperatorName(self):
        return self.SchemeOperatorName
    def set_SchemeOperatorName(self, SchemeOperatorName):
        self.SchemeOperatorName = SchemeOperatorName
    def get_SchemeTerritory(self):
        return self.SchemeTerritory
    def set_SchemeTerritory(self, SchemeTerritory):
        self.SchemeTerritory = SchemeTerritory
    def get_OtherQualifier(self):
        return self.OtherQualifier
    def set_OtherQualifier(self, OtherQualifier):
        self.OtherQualifier = OtherQualifier
    def add_OtherQualifier(self, value):
        self.OtherQualifier.append(value)
    def insert_OtherQualifier_at(self, index, value):
        self.OtherQualifier.insert(index, value)
    def replace_OtherQualifier_at(self, index, value):
        self.OtherQualifier[index] = value
    def has__content(self):
        if (
            self.URI is not None or
            self.TSPName is not None or
            self.SchemeOperatorName is not None or
            self.SchemeTerritory is not None or
            self.OtherQualifier
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TakenOverByType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TakenOverByType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TakenOverByType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TakenOverByType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TakenOverByType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TakenOverByType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='TakenOverByType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.URI is not None:
            namespaceprefix_ = self.URI_nsprefix_ + ':' if (UseCapturedNS_ and self.URI_nsprefix_) else ''
            self.URI.export(outfile, level, namespaceprefix_, namespacedef_='', name_='URI', pretty_print=pretty_print)
        if self.TSPName is not None:
            namespaceprefix_ = self.TSPName_nsprefix_ + ':' if (UseCapturedNS_ and self.TSPName_nsprefix_) else ''
            self.TSPName.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TSPName', pretty_print=pretty_print)
        if self.SchemeOperatorName is not None:
            namespaceprefix_ = self.SchemeOperatorName_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeOperatorName_nsprefix_) else ''
            self.SchemeOperatorName.export(outfile, level, namespaceprefix_='tsl:', namespacedef_='', name_='SchemeOperatorName', pretty_print=pretty_print)
        if self.SchemeTerritory is not None:
            namespaceprefix_ = self.SchemeTerritory_nsprefix_ + ':' if (UseCapturedNS_ and self.SchemeTerritory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSchemeTerritory>%s</%sSchemeTerritory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SchemeTerritory), input_name='SchemeTerritory')), namespaceprefix_ , eol_))
        for OtherQualifier_ in self.OtherQualifier:
            namespaceprefix_ = self.OtherQualifier_nsprefix_ + ':' if (UseCapturedNS_ and self.OtherQualifier_nsprefix_) else ''
            OtherQualifier_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OtherQualifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'URI':
            obj_ = NonEmptyMultiLangURIType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.URI = obj_
            obj_.original_tagname_ = 'URI'
        elif nodeName_ == 'TSPName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TSPName = obj_
            obj_.original_tagname_ = 'TSPName'
        elif nodeName_ == 'SchemeOperatorName':
            obj_ = InternationalNamesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SchemeOperatorName = obj_
            obj_.original_tagname_ = 'SchemeOperatorName'
        elif nodeName_ == 'SchemeTerritory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SchemeTerritory')
            value_ = self.gds_validate_string(value_, node, 'SchemeTerritory')
            self.SchemeTerritory = value_
            self.SchemeTerritory_nsprefix_ = child_.prefix
        elif nodeName_ == 'OtherQualifier':
            class_obj_ = self.get_class_obj_(child_, AnyType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OtherQualifier.append(obj_)
            obj_.original_tagname_ = 'OtherQualifier'
# end class TakenOverByType


class CertSubjectDNAttributeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, AttributeOID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        if AttributeOID is None:
            self.AttributeOID = []
        else:
            self.AttributeOID = AttributeOID
        self.AttributeOID_nsprefix_ = "tsl"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CertSubjectDNAttributeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CertSubjectDNAttributeType.subclass:
            return CertSubjectDNAttributeType.subclass(*args_, **kwargs_)
        else:
            return CertSubjectDNAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AttributeOID(self):
        return self.AttributeOID
    def set_AttributeOID(self, AttributeOID):
        self.AttributeOID = AttributeOID
    def add_AttributeOID(self, value):
        self.AttributeOID.append(value)
    def insert_AttributeOID_at(self, index, value):
        self.AttributeOID.insert(index, value)
    def replace_AttributeOID_at(self, index, value):
        self.AttributeOID[index] = value
    def has__content(self):
        if (
            self.AttributeOID
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='CertSubjectDNAttributeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CertSubjectDNAttributeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CertSubjectDNAttributeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertSubjectDNAttributeType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CertSubjectDNAttributeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CertSubjectDNAttributeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='CertSubjectDNAttributeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AttributeOID_ in self.AttributeOID:
            namespaceprefix_ = self.AttributeOID_nsprefix_ + ':' if (UseCapturedNS_ and self.AttributeOID_nsprefix_) else ''
            AttributeOID_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AttributeOID', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AttributeOID':
            obj_ = ObjectIdentifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AttributeOID.append(obj_)
            obj_.original_tagname_ = 'AttributeOID'
# end class CertSubjectDNAttributeType


class SignatureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SignedInfo = SignedInfo
        self.SignedInfo_nsprefix_ = "ds"
        self.SignatureValue = SignatureValue
        self.SignatureValue_nsprefix_ = "ds"
        self.KeyInfo = KeyInfo
        self.KeyInfo_nsprefix_ = "ds"
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
        self.Object_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureType.subclass:
            return SignatureType.subclass(*args_, **kwargs_)
        else:
            return SignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SignedInfo(self):
        return self.SignedInfo
    def set_SignedInfo(self, SignedInfo):
        self.SignedInfo = SignedInfo
    def get_SignatureValue(self):
        return self.SignatureValue
    def set_SignatureValue(self, SignatureValue):
        self.SignatureValue = SignatureValue
    def get_KeyInfo(self):
        return self.KeyInfo
    def set_KeyInfo(self, KeyInfo):
        self.KeyInfo = KeyInfo
    def get_Object(self):
        return self.Object
    def set_Object(self, Object):
        self.Object = Object
    def add_Object(self, value):
        self.Object.append(value)
    def insert_Object_at(self, index, value):
        self.Object.insert(index, value)
    def replace_Object_at(self, index, value):
        self.Object[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def has__content(self):
        if (
            self.SignedInfo is not None or
            self.SignatureValue is not None or
            self.KeyInfo is not None or
            self.Object
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignatureType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SignedInfo is not None:
            namespaceprefix_ = self.SignedInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.SignedInfo_nsprefix_) else ''
            self.SignedInfo.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfo', pretty_print=pretty_print)
        if self.SignatureValue is not None:
            namespaceprefix_ = self.SignatureValue_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureValue_nsprefix_) else ''
            self.SignatureValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValue', pretty_print=pretty_print)
        if self.KeyInfo is not None:
            namespaceprefix_ = self.KeyInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyInfo_nsprefix_) else ''
            self.KeyInfo.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfo', pretty_print=pretty_print)
        for Object_ in self.Object:
            namespaceprefix_ = self.Object_nsprefix_ + ':' if (UseCapturedNS_ and self.Object_nsprefix_) else ''
            Object_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Object', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignedInfo':
            obj_ = SignedInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignedInfo = obj_
            obj_.original_tagname_ = 'SignedInfo'
        elif nodeName_ == 'SignatureValue':
            obj_ = SignatureValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureValue = obj_
            obj_.original_tagname_ = 'SignatureValue'
        elif nodeName_ == 'KeyInfo':
            obj_ = KeyInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyInfo = obj_
            obj_.original_tagname_ = 'KeyInfo'
        elif nodeName_ == 'Object':
            obj_ = ObjectType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Object.append(obj_)
            obj_.original_tagname_ = 'Object'
# end class SignatureType


class SignatureValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureValueType.subclass:
            return SignatureValueType.subclass(*args_, **kwargs_)
        else:
            return SignatureValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignatureValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureValueType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureValueType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureValueType


class SignedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.CanonicalizationMethod = CanonicalizationMethod
        self.CanonicalizationMethod_nsprefix_ = "ds"
        self.SignatureMethod = SignatureMethod
        self.SignatureMethod_nsprefix_ = "ds"
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignedInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignedInfoType.subclass:
            return SignedInfoType.subclass(*args_, **kwargs_)
        else:
            return SignedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CanonicalizationMethod(self):
        return self.CanonicalizationMethod
    def set_CanonicalizationMethod(self, CanonicalizationMethod):
        self.CanonicalizationMethod = CanonicalizationMethod
    def get_SignatureMethod(self):
        return self.SignatureMethod
    def set_SignatureMethod(self, SignatureMethod):
        self.SignatureMethod = SignatureMethod
    def get_Reference(self):
        return self.Reference
    def set_Reference(self, Reference):
        self.Reference = Reference
    def add_Reference(self, value):
        self.Reference.append(value)
    def insert_Reference_at(self, index, value):
        self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value):
        self.Reference[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def has__content(self):
        if (
            self.CanonicalizationMethod is not None or
            self.SignatureMethod is not None or
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignedInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignedInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignedInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignedInfoType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CanonicalizationMethod is not None:
            namespaceprefix_ = self.CanonicalizationMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.CanonicalizationMethod_nsprefix_) else ''
            self.CanonicalizationMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='CanonicalizationMethod', pretty_print=pretty_print)
        if self.SignatureMethod is not None:
            namespaceprefix_ = self.SignatureMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureMethod_nsprefix_) else ''
            self.SignatureMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureMethod', pretty_print=pretty_print)
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CanonicalizationMethod':
            obj_ = CanonicalizationMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CanonicalizationMethod = obj_
            obj_.original_tagname_ = 'CanonicalizationMethod'
        elif nodeName_ == 'SignatureMethod':
            obj_ = SignatureMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureMethod = obj_
            obj_.original_tagname_ = 'SignatureMethod'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class SignedInfoType


class CanonicalizationMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CanonicalizationMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CanonicalizationMethodType.subclass:
            return CanonicalizationMethodType.subclass(*args_, **kwargs_)
        else:
            return CanonicalizationMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='CanonicalizationMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CanonicalizationMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CanonicalizationMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CanonicalizationMethodType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class CanonicalizationMethodType


class SignatureMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        self.HMACOutputLength = HMACOutputLength
        self.validate_HMACOutputLengthType(self.HMACOutputLength)
        self.HMACOutputLength_nsprefix_ = "ds"
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureMethodType.subclass:
            return SignatureMethodType.subclass(*args_, **kwargs_)
        else:
            return SignatureMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_HMACOutputLength(self):
        return self.HMACOutputLength
    def set_HMACOutputLength(self, HMACOutputLength):
        self.HMACOutputLength = HMACOutputLength
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_HMACOutputLengthType(self, value):
        result = True
        # Validate type HMACOutputLengthType, a restriction on integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def has__content(self):
        if (
            self.HMACOutputLength is not None or
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='SignatureMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureMethodType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HMACOutputLength is not None:
            namespaceprefix_ = self.HMACOutputLength_nsprefix_ + ':' if (UseCapturedNS_ and self.HMACOutputLength_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHMACOutputLength>%s</%sHMACOutputLength>%s' % (namespaceprefix_ , self.gds_format_integer(self.HMACOutputLength, input_name='HMACOutputLength'), namespaceprefix_ , eol_))
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'HMACOutputLength' and child_.text is not None:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'HMACOutputLength')
            ival_ = self.gds_validate_integer(ival_, node, 'HMACOutputLength')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeInteger, 'HMACOutputLength', ival_)
            self.content_.append(obj_)
            self.HMACOutputLength_nsprefix_ = child_.prefix
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SignatureMethodType


class ReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = "ds"
        self.DigestMethod = DigestMethod
        self.DigestMethod_nsprefix_ = "ds"
        self.DigestValue = DigestValue
        self.DigestValue_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transforms(self):
        return self.Transforms
    def set_Transforms(self, Transforms):
        self.Transforms = Transforms
    def get_DigestMethod(self):
        return self.DigestMethod
    def set_DigestMethod(self, DigestMethod):
        self.DigestMethod = DigestMethod
    def get_DigestValue(self):
        return self.DigestValue
    def set_DigestValue(self, DigestValue):
        self.DigestValue = DigestValue
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def has__content(self):
        if (
            self.Transforms is not None or
            self.DigestMethod is not None or
            self.DigestValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='ReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ReferenceType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transforms', pretty_print=pretty_print)
        if self.DigestMethod is not None:
            namespaceprefix_ = self.DigestMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestMethod_nsprefix_) else ''
            self.DigestMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestMethod', pretty_print=pretty_print)
        if self.DigestValue is not None:
            namespaceprefix_ = self.DigestValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestValue_nsprefix_) else ''
            self.DigestValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestValue', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
        elif nodeName_ == 'DigestMethod':
            obj_ = DigestMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestMethod = obj_
            obj_.original_tagname_ = 'DigestMethod'
        elif nodeName_ == 'DigestValue':
            obj_ = DigestValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestValue = obj_
            obj_.original_tagname_ = 'DigestValue'
# end class ReferenceType


class TransformsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Transform=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        if Transform is None:
            self.Transform = []
        else:
            self.Transform = Transform
        self.Transform_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformsType.subclass:
            return TransformsType.subclass(*args_, **kwargs_)
        else:
            return TransformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transform(self):
        return self.Transform
    def set_Transform(self, Transform):
        self.Transform = Transform
    def add_Transform(self, value):
        self.Transform.append(value)
    def insert_Transform_at(self, index, value):
        self.Transform.insert(index, value)
    def replace_Transform_at(self, index, value):
        self.Transform[index] = value
    def has__content(self):
        if (
            self.Transform
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='TransformsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformsType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='TransformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transform_ in self.Transform:
            namespaceprefix_ = self.Transform_nsprefix_ + ':' if (UseCapturedNS_ and self.Transform_nsprefix_) else ''
            Transform_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transform', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType


class TransformType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        if XPath is None:
            self.XPath = []
        else:
            self.XPath = XPath
        self.XPath_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformType.subclass:
            return TransformType.subclass(*args_, **kwargs_)
        else:
            return TransformType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_XPath(self):
        return self.XPath
    def set_XPath(self, XPath):
        self.XPath = XPath
    def add_XPath(self, value):
        self.XPath.append(value)
    def insert_XPath_at(self, index, value):
        self.XPath.insert(index, value)
    def replace_XPath_at(self, index, value):
        self.XPath[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.anytypeobjs_ is not None or
            self.XPath or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TransformType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TransformType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for XPath_ in self.XPath:
            namespaceprefix_ = self.XPath_nsprefix_ + ':' if (UseCapturedNS_ and self.XPath_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sXPath>%s</%sXPath>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(XPath_), input_name='XPath')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        elif nodeName_ == 'XPath' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'XPath')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'XPath')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'XPath', valuestr_)
            self.content_.append(obj_)
            self.XPath_nsprefix_ = child_.prefix
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class TransformType


class DigestMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestMethodType.subclass:
            return DigestMethodType.subclass(*args_, **kwargs_)
        else:
            return DigestMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='DigestMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestMethodType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class DigestMethodType


class KeyInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if KeyName is None:
            self.KeyName = []
        else:
            self.KeyName = KeyName
        self.KeyName_nsprefix_ = "ds"
        if KeyValue is None:
            self.KeyValue = []
        else:
            self.KeyValue = KeyValue
        self.KeyValue_nsprefix_ = "ds"
        if RetrievalMethod is None:
            self.RetrievalMethod = []
        else:
            self.RetrievalMethod = RetrievalMethod
        self.RetrievalMethod_nsprefix_ = "ds"
        if X509Data is None:
            self.X509Data = []
        else:
            self.X509Data = X509Data
        self.X509Data_nsprefix_ = "ds"
        if PGPData is None:
            self.PGPData = []
        else:
            self.PGPData = PGPData
        self.PGPData_nsprefix_ = "ds"
        if SPKIData is None:
            self.SPKIData = []
        else:
            self.SPKIData = SPKIData
        self.SPKIData_nsprefix_ = "ds"
        if MgmtData is None:
            self.MgmtData = []
        else:
            self.MgmtData = MgmtData
        self.MgmtData_nsprefix_ = "ds"
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyInfoType.subclass:
            return KeyInfoType.subclass(*args_, **kwargs_)
        else:
            return KeyInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_KeyName(self):
        return self.KeyName
    def set_KeyName(self, KeyName):
        self.KeyName = KeyName
    def add_KeyName(self, value):
        self.KeyName.append(value)
    def insert_KeyName_at(self, index, value):
        self.KeyName.insert(index, value)
    def replace_KeyName_at(self, index, value):
        self.KeyName[index] = value
    def get_KeyValue(self):
        return self.KeyValue
    def set_KeyValue(self, KeyValue):
        self.KeyValue = KeyValue
    def add_KeyValue(self, value):
        self.KeyValue.append(value)
    def insert_KeyValue_at(self, index, value):
        self.KeyValue.insert(index, value)
    def replace_KeyValue_at(self, index, value):
        self.KeyValue[index] = value
    def get_RetrievalMethod(self):
        return self.RetrievalMethod
    def set_RetrievalMethod(self, RetrievalMethod):
        self.RetrievalMethod = RetrievalMethod
    def add_RetrievalMethod(self, value):
        self.RetrievalMethod.append(value)
    def insert_RetrievalMethod_at(self, index, value):
        self.RetrievalMethod.insert(index, value)
    def replace_RetrievalMethod_at(self, index, value):
        self.RetrievalMethod[index] = value
    def get_X509Data(self):
        return self.X509Data
    def set_X509Data(self, X509Data):
        self.X509Data = X509Data
    def add_X509Data(self, value):
        self.X509Data.append(value)
    def insert_X509Data_at(self, index, value):
        self.X509Data.insert(index, value)
    def replace_X509Data_at(self, index, value):
        self.X509Data[index] = value
    def get_PGPData(self):
        return self.PGPData
    def set_PGPData(self, PGPData):
        self.PGPData = PGPData
    def add_PGPData(self, value):
        self.PGPData.append(value)
    def insert_PGPData_at(self, index, value):
        self.PGPData.insert(index, value)
    def replace_PGPData_at(self, index, value):
        self.PGPData[index] = value
    def get_SPKIData(self):
        return self.SPKIData
    def set_SPKIData(self, SPKIData):
        self.SPKIData = SPKIData
    def add_SPKIData(self, value):
        self.SPKIData.append(value)
    def insert_SPKIData_at(self, index, value):
        self.SPKIData.insert(index, value)
    def replace_SPKIData_at(self, index, value):
        self.SPKIData[index] = value
    def get_MgmtData(self):
        return self.MgmtData
    def set_MgmtData(self, MgmtData):
        self.MgmtData = MgmtData
    def add_MgmtData(self, value):
        self.MgmtData.append(value)
    def insert_MgmtData_at(self, index, value):
        self.MgmtData.insert(index, value)
    def replace_MgmtData_at(self, index, value):
        self.MgmtData[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.KeyName or
            self.KeyValue or
            self.RetrievalMethod or
            self.X509Data or
            self.PGPData or
            self.SPKIData or
            self.MgmtData or
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='KeyInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyInfoType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for KeyName_ in self.KeyName:
            namespaceprefix_ = self.KeyName_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sKeyName>%s</%sKeyName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(KeyName_), input_name='KeyName')), namespaceprefix_ , eol_))
        for KeyValue_ in self.KeyValue:
            namespaceprefix_ = self.KeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyValue_nsprefix_) else ''
            KeyValue_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValue', pretty_print=pretty_print)
        for RetrievalMethod_ in self.RetrievalMethod:
            namespaceprefix_ = self.RetrievalMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.RetrievalMethod_nsprefix_) else ''
            RetrievalMethod_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RetrievalMethod', pretty_print=pretty_print)
        for X509Data_ in self.X509Data:
            namespaceprefix_ = self.X509Data_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Data_nsprefix_) else ''
            X509Data_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509Data', pretty_print=pretty_print)
        for PGPData_ in self.PGPData:
            namespaceprefix_ = self.PGPData_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPData_nsprefix_) else ''
            PGPData_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='PGPData', pretty_print=pretty_print)
        for SPKIData_ in self.SPKIData:
            namespaceprefix_ = self.SPKIData_nsprefix_ + ':' if (UseCapturedNS_ and self.SPKIData_nsprefix_) else ''
            SPKIData_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SPKIData', pretty_print=pretty_print)
        for MgmtData_ in self.MgmtData:
            namespaceprefix_ = self.MgmtData_nsprefix_ + ':' if (UseCapturedNS_ and self.MgmtData_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMgmtData>%s</%sMgmtData>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(MgmtData_), input_name='MgmtData')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KeyName' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'KeyName')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'KeyName')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'KeyName', valuestr_)
            self.content_.append(obj_)
            self.KeyName_nsprefix_ = child_.prefix
        elif nodeName_ == 'KeyValue':
            obj_ = KeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'KeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_KeyValue'):
              self.add_KeyValue(obj_.value)
            elif hasattr(self, 'set_KeyValue'):
              self.set_KeyValue(obj_.value)
        elif nodeName_ == 'RetrievalMethod':
            obj_ = RetrievalMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RetrievalMethod', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RetrievalMethod'):
              self.add_RetrievalMethod(obj_.value)
            elif hasattr(self, 'set_RetrievalMethod'):
              self.set_RetrievalMethod(obj_.value)
        elif nodeName_ == 'X509Data':
            obj_ = X509DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'X509Data', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_X509Data'):
              self.add_X509Data(obj_.value)
            elif hasattr(self, 'set_X509Data'):
              self.set_X509Data(obj_.value)
        elif nodeName_ == 'PGPData':
            obj_ = PGPDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'PGPData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_PGPData'):
              self.add_PGPData(obj_.value)
            elif hasattr(self, 'set_PGPData'):
              self.set_PGPData(obj_.value)
        elif nodeName_ == 'SPKIData':
            obj_ = SPKIDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SPKIData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SPKIData'):
              self.add_SPKIData(obj_.value)
            elif hasattr(self, 'set_SPKIData'):
              self.set_SPKIData(obj_.value)
        elif nodeName_ == 'MgmtData' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'MgmtData')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'MgmtData')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'MgmtData', valuestr_)
            self.content_.append(obj_)
            self.MgmtData_nsprefix_ = child_.prefix
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class KeyInfoType


class KeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.DSAKeyValue = DSAKeyValue
        self.DSAKeyValue_nsprefix_ = "ds"
        self.RSAKeyValue = RSAKeyValue
        self.RSAKeyValue_nsprefix_ = "ds"
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyValueType.subclass:
            return KeyValueType.subclass(*args_, **kwargs_)
        else:
            return KeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DSAKeyValue(self):
        return self.DSAKeyValue
    def set_DSAKeyValue(self, DSAKeyValue):
        self.DSAKeyValue = DSAKeyValue
    def get_RSAKeyValue(self):
        return self.RSAKeyValue
    def set_RSAKeyValue(self, RSAKeyValue):
        self.RSAKeyValue = RSAKeyValue
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.DSAKeyValue is not None or
            self.RSAKeyValue is not None or
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='KeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyValueType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='KeyValueType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DSAKeyValue is not None:
            namespaceprefix_ = self.DSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DSAKeyValue_nsprefix_) else ''
            self.DSAKeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DSAKeyValue', pretty_print=pretty_print)
        if self.RSAKeyValue is not None:
            namespaceprefix_ = self.RSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.RSAKeyValue_nsprefix_) else ''
            self.RSAKeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RSAKeyValue', pretty_print=pretty_print)
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DSAKeyValue':
            obj_ = DSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DSAKeyValue'):
              self.add_DSAKeyValue(obj_.value)
            elif hasattr(self, 'set_DSAKeyValue'):
              self.set_DSAKeyValue(obj_.value)
        elif nodeName_ == 'RSAKeyValue':
            obj_ = RSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RSAKeyValue'):
              self.add_RSAKeyValue(obj_.value)
            elif hasattr(self, 'set_RSAKeyValue'):
              self.set_RSAKeyValue(obj_.value)
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class KeyValueType


class RetrievalMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, Type=None, Transforms=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetrievalMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetrievalMethodType.subclass:
            return RetrievalMethodType.subclass(*args_, **kwargs_)
        else:
            return RetrievalMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transforms(self):
        return self.Transforms
    def set_Transforms(self, Transforms):
        self.Transforms = Transforms
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def has__content(self):
        if (
            self.Transforms is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='RetrievalMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetrievalMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetrievalMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetrievalMethodType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetrievalMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='RetrievalMethodType'):
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='RetrievalMethodType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transforms', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
# end class RetrievalMethodType


class X509DataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if X509IssuerSerial is None:
            self.X509IssuerSerial = []
        else:
            self.X509IssuerSerial = X509IssuerSerial
        self.X509IssuerSerial_nsprefix_ = "ds"
        if X509SKI is None:
            self.X509SKI = []
        else:
            self.X509SKI = X509SKI
        self.X509SKI_nsprefix_ = None
        if X509SubjectName is None:
            self.X509SubjectName = []
        else:
            self.X509SubjectName = X509SubjectName
        self.X509SubjectName_nsprefix_ = None
        if X509Certificate is None:
            self.X509Certificate = []
        else:
            self.X509Certificate = X509Certificate
        self.X509Certificate_nsprefix_ = None
        if X509CRL is None:
            self.X509CRL = []
        else:
            self.X509CRL = X509CRL
        self.X509CRL_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509DataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509DataType.subclass:
            return X509DataType.subclass(*args_, **kwargs_)
        else:
            return X509DataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_X509IssuerSerial(self):
        return self.X509IssuerSerial
    def set_X509IssuerSerial(self, X509IssuerSerial):
        self.X509IssuerSerial = X509IssuerSerial
    def add_X509IssuerSerial(self, value):
        self.X509IssuerSerial.append(value)
    def insert_X509IssuerSerial_at(self, index, value):
        self.X509IssuerSerial.insert(index, value)
    def replace_X509IssuerSerial_at(self, index, value):
        self.X509IssuerSerial[index] = value
    def get_X509SKI(self):
        return self.X509SKI
    def set_X509SKI(self, X509SKI):
        self.X509SKI = X509SKI
    def add_X509SKI(self, value):
        self.X509SKI.append(value)
    def insert_X509SKI_at(self, index, value):
        self.X509SKI.insert(index, value)
    def replace_X509SKI_at(self, index, value):
        self.X509SKI[index] = value
    def get_X509SubjectName(self):
        return self.X509SubjectName
    def set_X509SubjectName(self, X509SubjectName):
        self.X509SubjectName = X509SubjectName
    def add_X509SubjectName(self, value):
        self.X509SubjectName.append(value)
    def insert_X509SubjectName_at(self, index, value):
        self.X509SubjectName.insert(index, value)
    def replace_X509SubjectName_at(self, index, value):
        self.X509SubjectName[index] = value
    def get_X509Certificate(self):
        return self.X509Certificate
    def set_X509Certificate(self, X509Certificate):
        self.X509Certificate = X509Certificate
    def add_X509Certificate(self, value):
        self.X509Certificate.append(value)
    def insert_X509Certificate_at(self, index, value):
        self.X509Certificate.insert(index, value)
    def replace_X509Certificate_at(self, index, value):
        self.X509Certificate[index] = value
    def get_X509CRL(self):
        return self.X509CRL
    def set_X509CRL(self, X509CRL):
        self.X509CRL = X509CRL
    def add_X509CRL(self, value):
        self.X509CRL.append(value)
    def insert_X509CRL_at(self, index, value):
        self.X509CRL.insert(index, value)
    def replace_X509CRL_at(self, index, value):
        self.X509CRL[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def has__content(self):
        if (
            self.X509IssuerSerial or
            self.X509SKI or
            self.X509SubjectName or
            self.X509Certificate or
            self.X509CRL or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='X509DataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509DataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509DataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509DataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509DataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='X509DataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for X509IssuerSerial_ in self.X509IssuerSerial:
            namespaceprefix_ = self.X509IssuerSerial_nsprefix_ + ':' if (UseCapturedNS_ and self.X509IssuerSerial_nsprefix_) else ''
            X509IssuerSerial_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='X509IssuerSerial', pretty_print=pretty_print)
        for X509SKI_ in self.X509SKI:
            namespaceprefix_ = self.X509SKI_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SKI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SKI>%s</%sX509SKI>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509SKI_), input_name='X509SKI')), namespaceprefix_ , eol_))
        for X509SubjectName_ in self.X509SubjectName:
            namespaceprefix_ = self.X509SubjectName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SubjectName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SubjectName>%s</%sX509SubjectName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509SubjectName_), input_name='X509SubjectName')), namespaceprefix_ , eol_))
        for X509Certificate_ in self.X509Certificate:
            namespaceprefix_ = self.X509Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509Certificate>%s</%sX509Certificate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509Certificate_), input_name='X509Certificate')), namespaceprefix_ , eol_))
        for X509CRL_ in self.X509CRL:
            namespaceprefix_ = self.X509CRL_nsprefix_ + ':' if (UseCapturedNS_ and self.X509CRL_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509CRL>%s</%sX509CRL>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509CRL_), input_name='X509CRL')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509IssuerSerial':
            obj_ = X509IssuerSerialType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.X509IssuerSerial.append(obj_)
            obj_.original_tagname_ = 'X509IssuerSerial'
        elif nodeName_ == 'X509SKI':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SKI')
            value_ = self.gds_validate_string(value_, node, 'X509SKI')
            self.X509SKI.append(value_)
            self.X509SKI_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SubjectName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SubjectName')
            value_ = self.gds_validate_string(value_, node, 'X509SubjectName')
            self.X509SubjectName.append(value_)
            self.X509SubjectName_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509Certificate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509Certificate')
            value_ = self.gds_validate_string(value_, node, 'X509Certificate')
            self.X509Certificate.append(value_)
            self.X509Certificate_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509CRL':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509CRL')
            value_ = self.gds_validate_string(value_, node, 'X509CRL')
            self.X509CRL.append(value_)
            self.X509CRL_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'X509DataType')
            self.set_anytypeobjs_(content_)
# end class X509DataType


class X509IssuerSerialType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, X509IssuerName=None, X509SerialNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.X509IssuerName = X509IssuerName
        self.X509IssuerName_nsprefix_ = None
        self.X509SerialNumber = X509SerialNumber
        self.X509SerialNumber_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509IssuerSerialType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509IssuerSerialType.subclass:
            return X509IssuerSerialType.subclass(*args_, **kwargs_)
        else:
            return X509IssuerSerialType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_X509IssuerName(self):
        return self.X509IssuerName
    def set_X509IssuerName(self, X509IssuerName):
        self.X509IssuerName = X509IssuerName
    def get_X509SerialNumber(self):
        return self.X509SerialNumber
    def set_X509SerialNumber(self, X509SerialNumber):
        self.X509SerialNumber = X509SerialNumber
    def has__content(self):
        if (
            self.X509IssuerName is not None or
            self.X509SerialNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='X509IssuerSerialType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509IssuerSerialType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509IssuerSerialType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509IssuerSerialType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509IssuerSerialType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509IssuerSerialType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='X509IssuerSerialType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509IssuerName is not None:
            namespaceprefix_ = self.X509IssuerName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509IssuerName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509IssuerName>%s</%sX509IssuerName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509IssuerName), input_name='X509IssuerName')), namespaceprefix_ , eol_))
        if self.X509SerialNumber is not None:
            namespaceprefix_ = self.X509SerialNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SerialNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SerialNumber>%s</%sX509SerialNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509SerialNumber), input_name='X509SerialNumber')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509IssuerName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509IssuerName')
            value_ = self.gds_validate_string(value_, node, 'X509IssuerName')
            self.X509IssuerName = value_
            self.X509IssuerName_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SerialNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SerialNumber')
            value_ = self.gds_validate_string(value_, node, 'X509SerialNumber')
            self.X509SerialNumber = value_
            self.X509SerialNumber_nsprefix_ = child_.prefix
# end class X509IssuerSerialType


class PGPDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.PGPKeyID = PGPKeyID
        self.PGPKeyID_nsprefix_ = None
        self.PGPKeyPacket = PGPKeyPacket
        self.PGPKeyPacket_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PGPDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PGPDataType.subclass:
            return PGPDataType.subclass(*args_, **kwargs_)
        else:
            return PGPDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PGPKeyID(self):
        return self.PGPKeyID
    def set_PGPKeyID(self, PGPKeyID):
        self.PGPKeyID = PGPKeyID
    def get_PGPKeyPacket(self):
        return self.PGPKeyPacket
    def set_PGPKeyPacket(self, PGPKeyPacket):
        self.PGPKeyPacket = PGPKeyPacket
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def has__content(self):
        if (
            self.PGPKeyID is not None or
            self.PGPKeyPacket is not None or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='PGPDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PGPDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PGPDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PGPDataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PGPDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='PGPDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='PGPDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PGPKeyID is not None:
            namespaceprefix_ = self.PGPKeyID_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPKeyID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPGPKeyID>%s</%sPGPKeyID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PGPKeyID), input_name='PGPKeyID')), namespaceprefix_ , eol_))
        if self.PGPKeyPacket is not None:
            namespaceprefix_ = self.PGPKeyPacket_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPKeyPacket_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPGPKeyPacket>%s</%sPGPKeyPacket>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PGPKeyPacket), input_name='PGPKeyPacket')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PGPKeyID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PGPKeyID')
            value_ = self.gds_validate_string(value_, node, 'PGPKeyID')
            self.PGPKeyID = value_
            self.PGPKeyID_nsprefix_ = child_.prefix
        elif nodeName_ == 'PGPKeyPacket':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PGPKeyPacket')
            value_ = self.gds_validate_string(value_, node, 'PGPKeyPacket')
            self.PGPKeyPacket = value_
            self.PGPKeyPacket_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'PGPDataType')
            self.anytypeobjs_.append(content_)
# end class PGPDataType


class SPKIDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SPKISexp=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if SPKISexp is None:
            self.SPKISexp = []
        else:
            self.SPKISexp = SPKISexp
        self.SPKISexp_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SPKIDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SPKIDataType.subclass:
            return SPKIDataType.subclass(*args_, **kwargs_)
        else:
            return SPKIDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SPKISexp(self):
        return self.SPKISexp
    def set_SPKISexp(self, SPKISexp):
        self.SPKISexp = SPKISexp
    def add_SPKISexp(self, value):
        self.SPKISexp.append(value)
    def insert_SPKISexp_at(self, index, value):
        self.SPKISexp.insert(index, value)
    def replace_SPKISexp_at(self, index, value):
        self.SPKISexp[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def has__content(self):
        if (
            self.SPKISexp or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='SPKIDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SPKIDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SPKIDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SPKIDataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SPKIDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SPKIDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='SPKIDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SPKISexp_ in self.SPKISexp:
            namespaceprefix_ = self.SPKISexp_nsprefix_ + ':' if (UseCapturedNS_ and self.SPKISexp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSPKISexp>%s</%sSPKISexp>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(SPKISexp_), input_name='SPKISexp')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SPKISexp':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SPKISexp')
            value_ = self.gds_validate_string(value_, node, 'SPKISexp')
            self.SPKISexp.append(value_)
            self.SPKISexp_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'SPKIDataType')
            self.set_anytypeobjs_(content_)
# end class SPKIDataType


class ObjectType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, _prefix=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tslx"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ ="tslx"
        self._prefix = _cast(None, _prefix)
        self._prefix_nsprefix_ = None
        self.Encoding = _cast(None, Encoding)
        self.Encoding_nsprefix_ = "tslx"
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectType.subclass:
            return ObjectType.subclass(*args_, **kwargs_)
        else:
            return ObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get__prefix(self):
        return self._prefix
    def set__prefix(self, _prefix):
        self._prefix = _prefix
    def get_Encoding(self):
        return self.Encoding
    def set_Encoding(self, Encoding):
        self.Encoding = Encoding
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tslx:', namespacedef_='xmlns:tslx="http://uri.etsi.org/02231/v2/additionaltypes#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='ObjectType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tslx:', name_='ObjectType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self._prefix is not None and '_prefix' not in already_processed:
            already_processed.add('_prefix')
            outfile.write(' _prefix=%s' % (quote_attrib(self._prefix), ))
        if self.Encoding is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            outfile.write(' Encoding=%s' % (quote_attrib(self.Encoding), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='tslx:', namespacedef_='xmlns:tslx="http://uri.etsi.org/02231/v2/additionaltypes#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='ObjectType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('_prefix', node)
        if value is not None and '_prefix' not in already_processed:
            already_processed.add('_prefix')
            self._prefix = value
        value = find_attr_value_('Encoding', node)
        if value is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            self.Encoding = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class ObjectType


class ManifestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestType.subclass:
            return ManifestType.subclass(*args_, **kwargs_)
        else:
            return ManifestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Reference(self):
        return self.Reference
    def set_Reference(self, Reference):
        self.Reference = Reference
    def add_Reference(self, value):
        self.Reference.append(value)
    def insert_Reference_at(self, index, value):
        self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value):
        self.Reference[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def has__content(self):
        if (
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='ManifestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ManifestType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='ManifestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class ManifestType


class SignaturePropertiesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignatureProperty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if SignatureProperty is None:
            self.SignatureProperty = []
        else:
            self.SignatureProperty = SignatureProperty
        self.SignatureProperty_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignaturePropertiesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignaturePropertiesType.subclass:
            return SignaturePropertiesType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SignatureProperty(self):
        return self.SignatureProperty
    def set_SignatureProperty(self, SignatureProperty):
        self.SignatureProperty = SignatureProperty
    def add_SignatureProperty(self, value):
        self.SignatureProperty.append(value)
    def insert_SignatureProperty_at(self, index, value):
        self.SignatureProperty.insert(index, value)
    def replace_SignatureProperty_at(self, index, value):
        self.SignatureProperty[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def has__content(self):
        if (
            self.SignatureProperty
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignaturePropertiesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignaturePropertiesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignaturePropertiesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignaturePropertiesType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignaturePropertiesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignaturePropertiesType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignaturePropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SignatureProperty_ in self.SignatureProperty:
            namespaceprefix_ = self.SignatureProperty_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureProperty_nsprefix_) else ''
            SignatureProperty_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureProperty', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignatureProperty':
            obj_ = SignaturePropertyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureProperty.append(obj_)
            obj_.original_tagname_ = 'SignatureProperty'
# end class SignaturePropertiesType


class SignaturePropertyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Target = _cast(None, Target)
        self.Target_nsprefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignaturePropertyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignaturePropertyType.subclass:
            return SignaturePropertyType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Target(self):
        return self.Target
    def set_Target(self, Target):
        self.Target = Target
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='SignaturePropertyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignaturePropertyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignaturePropertyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignaturePropertyType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignaturePropertyType'):
        if self.Target is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            outfile.write(' Target=%s' % (quote_attrib(self.Target), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='SignaturePropertyType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Target', node)
        if value is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            self.Target = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SignaturePropertyType


class DSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.P = P
        self.validate_CryptoBinary(self.P)
        self.P_nsprefix_ = "ds"
        self.Q = Q
        self.validate_CryptoBinary(self.Q)
        self.Q_nsprefix_ = "ds"
        self.G = G
        self.validate_CryptoBinary(self.G)
        self.G_nsprefix_ = "ds"
        self.Y = Y
        self.validate_CryptoBinary(self.Y)
        self.Y_nsprefix_ = "ds"
        self.J = J
        self.validate_CryptoBinary(self.J)
        self.J_nsprefix_ = "ds"
        self.Seed = Seed
        self.validate_CryptoBinary(self.Seed)
        self.Seed_nsprefix_ = "ds"
        self.PgenCounter = PgenCounter
        self.validate_CryptoBinary(self.PgenCounter)
        self.PgenCounter_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DSAKeyValueType.subclass:
            return DSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return DSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_P(self):
        return self.P
    def set_P(self, P):
        self.P = P
    def get_Q(self):
        return self.Q
    def set_Q(self, Q):
        self.Q = Q
    def get_G(self):
        return self.G
    def set_G(self, G):
        self.G = G
    def get_Y(self):
        return self.Y
    def set_Y(self, Y):
        self.Y = Y
    def get_J(self):
        return self.J
    def set_J(self, J):
        self.J = J
    def get_Seed(self):
        return self.Seed
    def set_Seed(self, Seed):
        self.Seed = Seed
    def get_PgenCounter(self):
        return self.PgenCounter
    def set_PgenCounter(self, PgenCounter):
        self.PgenCounter = PgenCounter
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def has__content(self):
        if (
            self.P is not None or
            self.Q is not None or
            self.G is not None or
            self.Y is not None or
            self.J is not None or
            self.Seed is not None or
            self.PgenCounter is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='DSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DSAKeyValueType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='DSAKeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='DSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.P is not None:
            namespaceprefix_ = self.P_nsprefix_ + ':' if (UseCapturedNS_ and self.P_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sP>%s</%sP>%s' % (namespaceprefix_ , self.gds_format_base64(self.P, input_name='P'), namespaceprefix_ , eol_))
        if self.Q is not None:
            namespaceprefix_ = self.Q_nsprefix_ + ':' if (UseCapturedNS_ and self.Q_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQ>%s</%sQ>%s' % (namespaceprefix_ , self.gds_format_base64(self.Q, input_name='Q'), namespaceprefix_ , eol_))
        if self.G is not None:
            namespaceprefix_ = self.G_nsprefix_ + ':' if (UseCapturedNS_ and self.G_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sG>%s</%sG>%s' % (namespaceprefix_ , self.gds_format_base64(self.G, input_name='G'), namespaceprefix_ , eol_))
        if self.Y is not None:
            namespaceprefix_ = self.Y_nsprefix_ + ':' if (UseCapturedNS_ and self.Y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sY>%s</%sY>%s' % (namespaceprefix_ , self.gds_format_base64(self.Y, input_name='Y'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_base64(self.J, input_name='J'), namespaceprefix_ , eol_))
        if self.Seed is not None:
            namespaceprefix_ = self.Seed_nsprefix_ + ':' if (UseCapturedNS_ and self.Seed_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSeed>%s</%sSeed>%s' % (namespaceprefix_ , self.gds_format_base64(self.Seed, input_name='Seed'), namespaceprefix_ , eol_))
        if self.PgenCounter is not None:
            namespaceprefix_ = self.PgenCounter_nsprefix_ + ':' if (UseCapturedNS_ and self.PgenCounter_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPgenCounter>%s</%sPgenCounter>%s' % (namespaceprefix_ , self.gds_format_base64(self.PgenCounter, input_name='PgenCounter'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'P':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'P')
            else:
                bval_ = None
            self.P = bval_
            self.P_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.P)
        elif nodeName_ == 'Q':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Q')
            else:
                bval_ = None
            self.Q = bval_
            self.Q_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Q)
        elif nodeName_ == 'G':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'G')
            else:
                bval_ = None
            self.G = bval_
            self.G_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.G)
        elif nodeName_ == 'Y':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Y')
            else:
                bval_ = None
            self.Y = bval_
            self.Y_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Y)
        elif nodeName_ == 'J':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'J')
            else:
                bval_ = None
            self.J = bval_
            self.J_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.J)
        elif nodeName_ == 'Seed':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Seed')
            else:
                bval_ = None
            self.Seed = bval_
            self.Seed_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Seed)
        elif nodeName_ == 'PgenCounter':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'PgenCounter')
            else:
                bval_ = None
            self.PgenCounter = bval_
            self.PgenCounter_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.PgenCounter)
# end class DSAKeyValueType


class RSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Modulus=None, Exponent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Modulus = Modulus
        self.validate_CryptoBinary(self.Modulus)
        self.Modulus_nsprefix_ = "ds"
        self.Exponent = Exponent
        self.validate_CryptoBinary(self.Exponent)
        self.Exponent_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RSAKeyValueType.subclass:
            return RSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return RSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Modulus(self):
        return self.Modulus
    def set_Modulus(self, Modulus):
        self.Modulus = Modulus
    def get_Exponent(self):
        return self.Exponent
    def set_Exponent(self, Exponent):
        self.Exponent = Exponent
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def has__content(self):
        if (
            self.Modulus is not None or
            self.Exponent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='RSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RSAKeyValueType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='RSAKeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='RSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Modulus is not None:
            namespaceprefix_ = self.Modulus_nsprefix_ + ':' if (UseCapturedNS_ and self.Modulus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sModulus>%s</%sModulus>%s' % (namespaceprefix_ , self.gds_format_base64(self.Modulus, input_name='Modulus'), namespaceprefix_ , eol_))
        if self.Exponent is not None:
            namespaceprefix_ = self.Exponent_nsprefix_ + ':' if (UseCapturedNS_ and self.Exponent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExponent>%s</%sExponent>%s' % (namespaceprefix_ , self.gds_format_base64(self.Exponent, input_name='Exponent'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Modulus':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Modulus')
            else:
                bval_ = None
            self.Modulus = bval_
            self.Modulus_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Modulus)
        elif nodeName_ == 'Exponent':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Exponent')
            else:
                bval_ = None
            self.Exponent = bval_
            self.Exponent_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Exponent)
# end class RSAKeyValueType


class NonEmptyURIType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonEmptyURIType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonEmptyURIType.subclass:
            return NonEmptyURIType.subclass(*args_, **kwargs_)
        else:
            return NonEmptyURIType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_NonEmptyURIType_impl(self, value):
        result = True
        # Validate type NonEmptyURIType_impl, a restriction on xsd:anyURI.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NonEmptyURIType_impl' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyURIType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonEmptyURIType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonEmptyURIType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonEmptyURIType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonEmptyURIType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyURIType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NonEmptyURIType


class DigestValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestValueType.subclass:
            return DigestValueType.subclass(*args_, **kwargs_)
        else:
            return DigestValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_DigestValueType_impl(self, value):
        result = True
        # Validate type DigestValueType_impl, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='DigestValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestValueType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigestValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='DigestValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DigestValueType


class NonEmptyMultiLangURIType(NonEmptyURIType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = NonEmptyURIType
    def __init__(self, lang=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tsl"
        super(globals().get("NonEmptyMultiLangURIType"), self).__init__(valueOf_,  **kwargs_)
        self.lang = _cast(None, lang)
        self.lang_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonEmptyMultiLangURIType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonEmptyMultiLangURIType.subclass:
            return NonEmptyMultiLangURIType.subclass(*args_, **kwargs_)
        else:
            return NonEmptyMultiLangURIType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def has__content(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            super(NonEmptyMultiLangURIType, self).has__content()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyMultiLangURIType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonEmptyMultiLangURIType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonEmptyMultiLangURIType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonEmptyMultiLangURIType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonEmptyMultiLangURIType'):
        super(NonEmptyMultiLangURIType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonEmptyMultiLangURIType')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' xml:lang=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lang), input_name='lang')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"', name_='NonEmptyMultiLangURIType', fromsubclass_=False, pretty_print=True):
        super(NonEmptyMultiLangURIType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        super(NonEmptyMultiLangURIType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NonEmptyMultiLangURIType


#
# End data representation classes.
#


GDSClassesMapping = {
    'AdditionalInformation': AdditionalInformationType,
    'AdditionalServiceInformation': AdditionalServiceInformationType,
    'CanonicalizationMethod': CanonicalizationMethodType,
    'CertSubjectDNAttribute': CertSubjectDNAttributeType,
    'DSAKeyValue': DSAKeyValueType,
    'DigestMethod': DigestMethodType,
    'DigestValue': DigestValueType,
    'DistributionPoints': NonEmptyURIListType,
    'ElectronicAddress': ElectronicAddressType,
    'ExtendedKeyUsage': ExtendedKeyUsageType,
    'Extension': ExtensionType,
    'KeyInfo': KeyInfoType,
    'KeyValue': KeyValueType,
    'Manifest': ManifestType,
    'NextUpdate': NextUpdateType,
    'Object': ObjectType,
    'OtherTSLPointer': OtherTSLPointerType,
    'PGPData': PGPDataType,
    'PointersToOtherTSL': OtherTSLPointersType,
    'PolicyOrLegalNotice': PolicyOrLegalnoticeType,
    'PostalAddress': PostalAddressType,
    'PostalAddresses': PostalAddressListType,
    'PublicKeyLocation': NonEmptyURIType,
    'Qualifications': QualificationsType,
    'RSAKeyValue': RSAKeyValueType,
    'Reference': ReferenceType,
    'RetrievalMethod': RetrievalMethodType,
    'SPKIData': SPKIDataType,
    'SchemeInformation': TSLSchemeInformationType,
    'SchemeInformationURI': NonEmptyMultiLangURIListType,
    'SchemeName': InternationalNamesType,
    'SchemeOperatorName': InternationalNamesType,
    'SchemeTypeCommunityRules': NonEmptyMultiLangURIListType,
    'ServiceDigitalIdentities': ServiceDigitalIdentityListType,
    'ServiceDigitalIdentity': DigitalIdentityListType,
    'ServiceHistory': ServiceHistoryType,
    'ServiceHistoryInstance': ServiceHistoryInstanceType,
    'ServiceInformation': TSPServiceInformationType,
    'ServiceStatus': NonEmptyURIType,
    'ServiceSupplyPoints': ServiceSupplyPointsType,
    'ServiceTypeIdentifier': NonEmptyURIType,
    'Signature': SignatureType,
    'SignatureMethod': SignatureMethodType,
    'SignatureProperties': SignaturePropertiesType,
    'SignatureProperty': SignaturePropertyType,
    'SignatureValue': SignatureValueType,
    'SignedInfo': SignedInfoType,
    'TSLType': NonEmptyURIType,
    'TSPInformation': TSPInformationType,
    'TSPService': TSPServiceType,
    'TSPServices': TSPServicesListType,
    'TakenOverBy': TakenOverByType,
    'Transform': TransformType,
    'Transforms': TransformsType,
    'TrustServiceProvider': TSPType,
    'TrustServiceProviderList': TrustServiceProviderListType,
    'TrustServiceStatusList': TrustStatusListType,
    'X509CertificateLocation': NonEmptyURIType,
    'X509Data': X509DataType,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:tsl="http://uri.etsi.org/02231/v2#"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from trustedlists_api import *\n\n')
        sys.stdout.write('import trustedlists_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}
