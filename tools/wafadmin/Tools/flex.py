#!/usr/bin/env python
# encoding: utf-8
# John O'Meara, 2006
# Thomas Nagy, 2006-2008

"Flex processing"

import TaskGen

def decide_ext(self, node):
	if 'cxx' in self.features: return '.lex.cc'
	else: return '.lex.c'

TaskGen.declare_chain(
	name = 'flex',
	rule = '${FLEX} -o${TGT} ${FLEXFLAGS} ${SRC}',
	ext_in = '.l',
	ext_out = '.c .cxx'
	decider = decide_ext,
)

def detect(conf):
	conf.find_program('flex', var='FLEX', mandatory=True)
	conf.env['FLEXFLAGS'] = ''

