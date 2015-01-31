def file_search(group,file_dict):
	hits = []
	for key in file_dict:
		if group in file_dict[key]['name'] or group in file_dict[key]['ext']:
			hits.append([key,file_dict[key]['name'],file_dict[key]['ext']])
	return hits

parse_data = { 
'spv_basic':'spv_basic spss output file',
'odt_basic':'odt_basic open office text document',
'csv_basic':'csv_basic comma-separated values',
'pxr_basic':'pxr_basic pixar image computer',
'stc_basic':'stc_basic open office xml spreadsheet template',
'uot_1':'uot_1 uniform office format text',
'raw_ps':'raw_ps photoshop raw file',
'ott_basic':'ott_basic open office text template',
'iff_basic':'iff_basic interchange file format',
'pcx_basic':'pcx_basic personal computer exchange',
'xml_basic':'xml_basic xml',
'js_basic':'js_basic javascript programming language',
'psd_basic':'psd_basic photoshop document',
'jpg_basic':'jpg_basic joint photographic experts group',
'svg_basic':'svg_basic scalable vector graphics',
'pbm_basic':'pbm_basic netpbm format',
'uot_2':'uot_2 uniform office format 2 text',
'r_basic':'r_basic r',
'docx_basic':'docx_basic open xml microsoft document',
'txt_basic':'txt_basic text file',
'png_basic':'png_basic portable network graphics',
'tiff_basic':'tiff_basic tagged image file format',
'psb_basic':'psb_basic photoshop file',
'ppt_basic':'ppt_basic microsoft powerpoint',
'doc_95':'doc_95 microsoft 95 document',
'dcm_basic':'dcm_basic digital imaging and communications in medicine',
'xls_basic':'xls_basic excel binary',
'python_basic':'python_basic python',
'rdata_basic':'rdata_basic stored r object',
'pct_basic':'pct_basic macintosh picture metafile',
'xlsx_basic':'xlsx_basic open xml microsoft spreadsheet',
'mako_basic':'mako_basic mako python template engine',
'uos_2':'uos_2 uniform office format 2 spreadsheetp',
'ipynb_basic':'ipynb_basic ipython notebook',
'dta_13':'dta_13 stata data version 13',
'r_basic':'r_basic r programming language',
'bmp_basic':'bmp_basic windows bitmap',
'doc_6':'doc_6 microsoft 6.0 document',
'css_basic':'css_basic css',
'psw_basic':'psw_basic pocket word',
'tga_basic':'tga_basic truevision tga',
'ods_basic':'ods_basic open office spreadsheet',
'slk_basic':'slk_basic symbolic link',
'sxw_basic':'sxw_basic open office xml text document',
'json_basic':'json_basic javascript object notation',
'gif_basic':'gif_basic graphics interchange format',
'dbf_basic':'dbf_basic database file',
'dta_12':'dta_12 stata data version 12',
'sxc_basic':'sxc_basic open office xml spreadsheet',
'ots_basic':'ots_basic open office spreadsheet template',
'pptx_basic':'pptx_basic open xml microsoft powerpoint',
'uos_1':'uos_1 uniform office format spreadsheet',
'pdb_palm':'pdb_palm aportisdoc (palm)',
'stw_basic':'stw_basic open office xml text template',
'doc_97_2000_xp':'doc_97_2000_xp microsoft 97, 2000, and xp document',
'xml_docbook':'xml_docbook xml docbook',
'txt_utf-8':'txt_utf-8 text file encoded as utf-8',
'html_basic':'html_basic hypertext markup language',
'dif_basic':'dif_basic data interchange format',
'pdf_basic':'pdf_basic portable document format',
'sav_basic':'sav_basic spss data',
'xml_word_2003':'xml_word_2003 microsoft word 2003 xml',
'rtf_basic':'rtf_basic rich text format',
'pdb_protein':'pdb_protein protein data bank file'}
