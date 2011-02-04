/*
 * Success del formulario para mostrar los errores. 
 */
function successForm(response, status, xhr, form){

    n = 0;
    
    /* remueve los errores anteriores */
    form.find(".fielderror, .fieldok").remove();
    
    /* mensaje de error para el formulario */
    if (__error__ = response.__error__) {
        delete response.__error__;
        form.prepend("<div class='fielderror'>" + __error__ + "</div>");
        n++;
    }
    
    /* mensaje final para el usuario */
    if (__success__ = response.__success__) {
        delete response.__success__;
    }
    
    jQuery.each(response, function(name, value){
        /* inserta los mensajes de errores */
        n++;
		form.find("* [id='" + form.attr("id") + "_" + name + "']").parent().
		append("<span class='fielderror'>" + value + "</span>");
    });
    
    if (n == 0) {
        /* no hay errores, con exito */
        if (__success__) 
            form.prepend("<div class='fieldok'>" + __success__ + "</div>");
		return true;
    }
	
	return false;
}


/* Con esto se puede manipular el success del formulario */
function success_form(response, status, xhr, form){
    if (successForm(response, status, xhr, form)) {
        form.clearForm();
    }
    else {
    }
}

/* Con esto se formatea el resultado del autocomplete si es enviado como json 
 * 	ejemplo(python):
 * 	import json
 * 	return json.JSONEncoder().encode([['paraguay'],['peru'],['panama'],['pakistan']])
 */
function autocomplete_parse(data){
    return $.map(data, function(row){
        return {
            data: row,
            value: row[0],
            result: row[0] // + " <" + row.to + ">"
        }
    });
}



