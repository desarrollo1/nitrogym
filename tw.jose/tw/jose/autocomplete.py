# -*- coding: utf-8 -*-


from base import *
from tw.jquery.base import *
#from tw.jquery.direction import *


#javascript=[JSLink(link='/js/jquery.ajaxQueue.js'),
#            JSLink(link='/js/jquery.bgiframe.min.js'),
#            JSLink(link='/js/thickbox-compressed.js'),]

jquery_autocomplete_js = JSLink(modname=__name__, filename='static/js/jquery.autocomplete.js', javascript=[jquery_extra_js])
jquery_autocomplete_css=CSSLink(modname=__name__, filename='static/css/jquery.autocomplete.css')


#jquery_autocomplete_js = JSLink(link='/js/jquery.autocomplete.js')
#
#jQuery= js_function('$')
#jquery_autocomplete_css=CSSLink(link='/css/jquery.autocomplete.css')


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
    parse = parse=js_function("autocomplete_parse")
    
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
    
        options = update_options(self, {}, d, *autocomplete_params)
        url_data = d.get('url_data', self.url_data)
        
        #call = js_function("$(function(){%s});" %
        call =  js_function('$("#%s").autocomplete' % d.id)(url_data, options) #)
        
        print call
        self.add_call(call)


