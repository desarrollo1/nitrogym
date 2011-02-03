# -*- coding: utf-8 -*-


from nitrogym.widgets.base import *
from tw.jquery.base import *
from tw.jquery.direction import *


#javascript=[JSLink(link='/js/jquery.ajaxQueue.js'),
#            JSLink(link='/js/jquery.bgiframe.min.js'),
#            JSLink(link='/js/thickbox-compressed.js'),]
jquery_autocomplete_js = JSLink(link='/js/jquery.autocomplete.js')
jQuery= js_function('$')
jquery_autocomplete_css=CSSLink(link='/css/jquery.autocomplete.css')


x = \
"""
function formatItem(data, i, n, value)
{
    //alert(data[0]);
    //return data[0];
    //return "<img src='/images/paises/" + data[0].toLowerCase() + ".png'/>" + data[0];
    
    return value;
}

function formatMatch(data, i, max) 
{
    return data.name;
}
        
        
function formatResult(data, value) {
    return data[0];
}

function parsear(data) {
            
            return $.map(data, function(row) {
                //alert(row[0]);
                
                return {
                    data: row,
                    value: row[0],
                    result: row[0] // + " <" + row.to + ">"
                }
            });
}
"""
test = JSSource(x)




autocomplete_params = ['url_data', 'formatItem', 'formatResult', 'formatMatch', 'dataType', 'parse',
              'mustMatch', 'matchContains', 'highlight', 'matchCase', 'matchSubset', 'extraFields',
              'cacheLength', 'autoFill', 'extraFields','extraParams', 'max', 'minChars', 'multiple',
              'multipleSeparator', 'scroll', 'scrollHeight', 'delay', 'selectFirst', 'size']

class AutoCompleteField(twf.FormField):
    """
    
    
    
    Obs: 
    1 - cuando se especifique en 'url_data' una url, el controlador debera retornar datos
        con formato (json) y se debera utilizar el parametro parse apuntando a una funcion 
        para ubicar el resultado, en otro caso un string con delimitador '\n' 
        Ej: 
        1 - import json
            ...
            @expose('json')
            ...
            return json.JSONEncoder().encode([['maria'], ['marina'], ['marta']])
        
        2 - @expose()
            ...
            return "Paraguay\nPeru\nPuerto rico"
    """
    
    
    params = autocomplete_params
    javascript=[jquery_autocomplete_js, test]
    css=[jquery_autocomplete_css]
    
    #url_data = '/persona/autocompletar'
    #url_data = js_function("'Argentina-brasil-paraguay-bolivia-chile-ecuador-peru-uruguay-venezuela-colombia'.split('-')")
#    url_data = js_function(['Argentina', 'Brasil'])
#    parse=js_function("parsear")
#    dataType = 'json'
#    formatItem = js_function("formatItem")
#    formatMatch = None #js_function("formatMatch")
#    formatResult = js_function("formatResult")
#    mustMatch = None # default False
#    matchContains = None # default False
#    highlight = None
#    matchCase = None # default False
#    matchSubset = None # default True
#    cacheLength = None # default 10
#    autoFill = None # default False
#    extraParams = None
#    max = None # default 10
#    minChars = None # default 1
#    multiple = None # default False
#    multipleSeparator = None # default ', '
#    selectFirst = None
#    delay = None
#    scrollHeight = None
#    scroll = None
#    extraFields = None
    
    template = \
    """
    <input type='text' xmlns="http://www.w3.org/1999/xhtml" 
                xmlns:py="http://genshi.edgewall.org/"
                id="${id}"
                name="${name}"
                class="${css_class}"
                py:attrs="attrs"
                value="${value}" />
    """
    def update_params(self, d):
        

        
        super(AutoCompleteField, self).update_params(d)

        
        if not getattr(d, "id", None):
            raise ValueError, "AutocompleteField is supposed to have id"
        
#        params = ['url_data', 'formatItem', 'formatResult', 'formatMatch', 'dataType', 'parse',
#              'mustMatch', 'matchContains', 'highlight', 'matchCase', 'matchSubset', 'extraFields',
#              'cacheLength', 'autoFill', 'extraParams', 'max', 'minChars', 'multiple',
#              'multipleSeparator', 'scroll', 'scrollHeight', 'delay', 'selectFirst', 'size']
    
        options = {}
        update_options(self, options, d, *autocomplete_params)
    
#        update_option(self, options, 'dataType', d)
#        update_option(self, options, 'parse', d)
#        update_option(self, options, 'formatItem', d)
#        update_option(self, options, 'formatMatch', d)
#        update_option(self, options, 'formatResult', d)
#        update_option(self, options, 'mustMatch', d)
#        update_option(self, options, 'matchContains', d)
#        update_option(self, options, 'matchCase', d)
#        update_option(self, options, 'matchSubset', d)
#        update_option(self, options, 'cacheLength', d)
#        update_option(self, options, 'autoFill', d)
#        update_option(self, options, 'extraParams', d)
#        update_option(self, options, 'extraFields', d)
#        update_option(self, options, 'max', d)
#        update_option(self, options, 'minChars', d)
#        update_option(self, options, 'multiple', d)
#        update_option(self, options, 'multipleSeparator', d)
#        update_option(self, options, 'highlight', d)
#        update_option(self, options, 'scroll', d)
#        update_option(self, options, 'scrollHeight', d)
#        update_option(self, options, 'delay', d)
#        update_option(self, options, 'selectFirst', d)
        url_data = d.get('url_data', self.url_data)
        
        call = js_function("$(function(){%s});" %
               js_function('$("#%s").autocomplete' % d.id)(url_data, options))
        
        print call
        self.add_call(call)


