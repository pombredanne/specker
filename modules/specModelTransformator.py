# -*- coding: utf-8 -*-
# ####################################################################
# specker-lib - spec file manipulation library
# Copyright (C) 2015  Fridolin Pokorny, fpokorny@redhat.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# ####################################################################
'''
An adapter used to communicate with model
@author: Fridolin Pokorny
@contact: fpokorny@redhat.com
@organization: Red Hat Inc.
@license: GPL 2.0
'''

from specModel import SpecModel

class SpecModelTransformator(object):
	'''
	An adapter used to communicate with model
	'''
	def __init__(self, model = None):
		if not model:
			self.model = SpecModel()
		else:
			self.model = model

	def set_model(self, model):
		'''
		Set model to manipulate with
		@param model: a spec model
		@type model: L{SpecModel}
		@return: None
		@rtype: None
		'''
		self.model = model

	def get_model(self):
		'''
		Get used spec model
		@return: spec model
		@rtype: L{SpecModel}
		'''
		return self.model

	def get_sections(self):
		'''
		Get list of all sections
		@return: list of sections
		@rtype: list of L{SpecSection}
		'''
		return self.model.get_sections()

