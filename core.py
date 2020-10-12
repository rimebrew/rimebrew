# env variables
# code truck used for prototype, the functions are getting split
# This file would eventually be deleted.


# Example meta bundle structure:
# {'luna_pinyin': {'display_name': '朙月拼音-默認',
#             'files': ['luna_pinyin.schema.yaml'],
#             'source': 'luna_pinyin.yaml'},
# 'luna_pinyin_simp': {'display_name': '朙月拼音-簡體',
#                  'files': ['luna_pinyin_simp.schema.yaml'],
#                  'source': 'luna_pinyin.yaml'},
#


# def schema_install(schema_name):
# meta_bundle[schema_name]

# now we begin to do real shits.

# for _name, schema in meta_bundle.items():
#     """
#     Schema's structure
#       display_name: 朙月拼音-默認
#       files:
#         - luna_pinyin.schema.yaml
#       source: luna_pinyin.yaml
#     """
#     _path= './rime_schemas-main'+'/'+schema['source']
#     with open(_path,'r') as _f:
#         _t=yaml.load(_f,Loader=yaml.Loader)
#         with open('./downloads/'+_name+'.yaml','w+') as _w:
#             download_url_to_path(_t['repository']['url']+_t['repository']['url_to_file'],'./downloads/'+_name+'.zip')
