import os

srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
    opt.tool_options('compiler_cxx')
    opt.tool_options('compiler_cc')


def configure(conf):
    conf.check_tool('compiler_cxx')
    conf.check_tool("compiler_cc")
    #conf.env.append_value('LINKFLAGS', ['-lgmp']);
    conf.check_tool('node_addon')
    conf.link_add_flags()

def build(bld):
    obj = bld.new_task_gen('cc','cxx',  'cshlib', 'node_addon')
    obj.cxxflags = [ "-O3", "-DICONV_CONST=const", "-DUSE_AIX=1","-DUSE_DOS=1", "-DUSE_EXTRA=1", "-DUSE_OSF1=1", '-DHAVE_WORKING_O_NOFOLLOW=1']
    obj.cxxflags.extend( ['-Wno-unused-function', '-Wno-unused-parameter', '-Wno-unused-variable'])
    obj.cflags = [ "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", '-Wno-unused-function', '-Wno-unused-parameter', '-Wno-unused-variable', '-DHAVE_WORKING_O_NOFOLLOW=1', '-DLIBDIR="."', '-DICONV_CONST=const', '-DUSE_AIX=1', '-DUSE_DOS=1', '-DUSE_EXTRA=1', '-DUSE_OSF1=1']
    obj.target = 'iconv'
    obj.source = "src/binding.cc deps/libiconv/lib/iconv.c deps/libiconv/libcharset/lib/localcharset.c"
    obj.includes = "deps/libiconv/srclib support"
