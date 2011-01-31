
function test_form(form)
{
	form.clearForm();
	alert('bye bue');
}



function successForm(responseText, statusText, xhr, form){

    n = 0;
    json = responseText;
    
    /* remueve los errores anteriores */
    form.find(".fielderror, .fieldok").remove();
    
    /* mensaje de error para el formulario */
    if (__error__ = json.__error__) {
        delete json.__error__;
        form.prepend("<div class='fielderror'>" + __error__ + "</div>");
        n++;
    }
    
    /* mensaje para el usuario */
    if (__success__ = json.__success__) {
        delete json.__success__;
    }
    
    jQuery.each(json, function(name, value){
        /* inserta los mensajes de errores */
        n++;
        form.find("td").has("* [name='" + name + "']").append("<span class='fielderror'>" + value + "</span>");
    });
    
    if (n == 0) {
        /* no hay errores, con exito */
        alert('hecho');
        if (__success__) 
            form.prepend("<div class='fieldok'>" + __success__ + "</div>");
        if (success = form.data('on_success')(form)) 
            on_success(form);
    }
}
