import os

srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
    opt.tool_options('compiler_cxx')

def configure(conf):
    conf.check_tool('compiler_cxx')
    #conf.env.append_value('LINKFLAGS', ['-lgmp']);
    conf.check_tool('node_addon')
    conf.link_add_flags()

def build(bld):
    obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
    obj.cxxflags = [ "-O3", "-DICONV_CONST=const", "-DUSE_AIX=1","-DUSE_DOS=1", "-DUSE_EXTRA=1", "-DUSE_OSF1=1", '-DHAVE_WORKING_O_NOFOLLOW=1']
    obj.cxxflags.extend( ['-Wno-unused-function', '-Wno-unused-parameter', '-Wno-unused-variable'])
    obj.target = 'iconv'
    obj.source = "src/binding.cc" #  deps/libiconv/libcharset/lib/localcharset.c deps/libiconv/lib/iconv.c"
    obj.includes = "deps/libiconv/srclib support"
