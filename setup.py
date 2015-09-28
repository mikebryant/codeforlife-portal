# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from setuptools import find_packages, setup

setup(name='portal',
      version='1.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'codeforlife-reports==1.0',
          'django==1.7',
          'django-appconf==0.6',
          'django-casper==0.0.2',
          'django-countries==3.3',
          'djangorestframework==2.3.9',
          'unittest2==0.5.1',
          'pyyaml==3.11',
          'six==1.6.1',
          'docutils==0.11',
          'django-recaptcha-field==1.0b2',
          'django-jquery==1.9.1',
          'postcodes==0.1',
          'django-two-factor-auth==1.0.0-beta3',
          'selenium==2.42.1',
          'urllib3==1.9',
          'reportlab==3.1.44',
          'requests==2.7.0',
          'responses==0.3.0'
      ],
      )
