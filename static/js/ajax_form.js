$(function() {

  Onload();
})

function Onload() {


if(document.getElementById('tickets_ewrop_info')){
  valide_form('#tickets_ewrop_info','.input-tickets__grops', '/create_europe_order/');
}

if(document.getElementById('bus_bus_order')){
  valide_form('#bus_bus_order','.input-tickets__grops','/create_bus_order/');
}

if(document.getElementById('form_contact_form')){
  valide_form('#form_contact_form','.input-tickets__grops','/create_contact/');
}
if(document.getElementsByClassName('form__coments_buss').length>0){
  $('.form__coments_buss').each(function(index, form) {
    // console.log(form.action);
    // console.log();
    valide_form_class(form,form.action);
  })
//   valide_form_class('.form__coments_buss','.input-tickets__grops' );
}

}

function location_leng() {
  return location.pathname.split('/')[1];
}

function valide_form(id_form, append_error_box,url_form ) {

var url_form_tab  = url_form;
  if ($(id_form).length > 0) {

    var lang_site;
    var errore_text = {};

    lang_site = location_leng();
    switch (lang_site) {
      case 'uk':
        errore_text.required = 'Поле обов\'язково для заповнення';
        errore_text.email = 'Поле має містити email';
        break;
      case 'ru':
        errore_text.required = 'Поле обязательно для заполнения';
        errore_text.email = 'Поле должно содержать email';
        break;
      case 'en':
        errore_text.required = 'The field is required';
        errore_text.email = 'The field must contain an email';
        break;
      default:
        errore_text.required = 'Поле обов\'язково для заповнення.';
        errore_text.email = 'Поле має містити email.';
    }


    $(id_form).validate({
      errorPlacement: function(event, validator) {
        console.log(validator);
        console.log(append_error_box);
        $(validator).parents(append_error_box).append($(event));
      },
      rules: {
        email: {
          required: true,
          email: true,
        },
        phone: {
          required: true,

        }
      },

      messages: {
        email: {
          required: errore_text.required,
          email: errore_text.email
        },
        phone: {
          required: errore_text.required,
        }
      },

      submitHandler: function(form) {
        console.log(url_form);
        console.log(id_form);
         form_ajax_static(id_form,url_form_tab);
      }
    });
  }

}




function valide_form_class(form,url_form){
  var lang_site;
  var errore_text = {};

  lang_site = location_leng();
  switch (lang_site) {
    case 'uk':
      errore_text.required = 'Поле обов\'язково для заповнення';
      errore_text.email = 'Поле має містити email';
      break;
    case 'ru':
      errore_text.required = 'Поле обязательно для заполнения';
      errore_text.email = 'Поле должно содержать email';
      break;
    case 'en':
      errore_text.required = 'The field is required';
      errore_text.email = 'The field must contain an email';
      break;
    default:
      errore_text.required = 'Поле обов\'язково для заповнення.';
      errore_text.email = 'Поле має містити email.';
  }


  $(form).validate({
    errorPlacement: function(event, validator) {
      console.log(validator);

      $(validator).parents('.input-tickets__grops').append($(event));

    },
    rules: {
      email: {
        required: true,
        email: true,
      },
      phone: {
        required: true,

      }
    },

    messages: {
      email: {
        required: errore_text.required,
        email: errore_text.email
      },
      phone: {
        required: errore_text.required,
      }
    },

    submitHandler: function(form) {

       form_ajax_static_class(form,url_form);
    }
  });
}










function form_ajax_static_class(form,url_form){

    var form_input, form_json={},url_form;
    var SITE_NAME = window.location.origin
    var url_form =   url_form;
    form_input = $(form).serializeArray();
    var flag_chesk = 0;
    $(form_input).each(function(index, obj) {
      form_json[obj.name] = obj.value;

    });
console.log("crash");

    $.ajax({
      url: url_form,
      type: 'POST',
      data:form_input,
      async: true,
      success: function(order) {
        $.fancybox.open({
          src: '#form_send_done_comment',
          type: 'inline',
          touch: false,
          autoStart: false,
          padding: 0,
          hideOnClose: false,
          showCloseButton: true,
          opts: {
            afterShow: function(instance, current) { }
          }
        })


      }
    })

}





















function form_ajax_static(id_form,url_form){


  var form_input, form_json={},url_form;
  var SITE_NAME = window.location.origin
  var url_form = SITE_NAME + url_form;
  form_input = $(id_form).serializeArray();
  var flag_chesk = 0;
  $(form_input).each(function(index, obj) {
    form_json[obj.name] = obj.value;

  });
// console.log(url_form);
// console.log(form_input);

  $.ajax({
    url: url_form,
    type: 'POST',
    data:form_input,
    async: true,
    success: function(order) {
      $.fancybox.open({
        src: '#form_send_done',
        type: 'inline',
        touch: false,
        autoStart: false,
        padding: 0,
        hideOnClose: false,
        showCloseButton: true,
        opts: {
          afterShow: function(instance, current) { }
        }
      })


    }
  })


}

function valide_form_order(id_form){
  console.log("crash");
  if ($(id_form).length > 0) {

    var lang_site;
    var errore_text = {};

    lang_site = location_leng();
    switch (lang_site) {
      case 'uk':
        errore_text.required = 'Поле обов\'язково для заповнення';
        errore_text.email = 'Поле має містити email';
        break;
      case 'ru':
        errore_text.required = 'Поле обязательно для заполнения';
        errore_text.email = 'Поле должно содержать email';
        break;
      case 'en':
        errore_text.required = 'The field is required';
        errore_text.email = 'The field must contain an email';
        break;
      default:
        errore_text.required = 'Поле обов\'язково для заповнення.';
        errore_text.email = 'Поле має містити email.';
    }


    $(id_form).validate({
      // errorPlacement: function(event, validator) {
      //   $(validator).parents(append_error_box).append($(event));
      // },
     //
     errorPlacement: function(event, validator) {
       $(validator).parents('.form-group').append($(event));
     },
      rules: {
        username: {
          required: true,
        },
        email: {
          required: true,
          email: true,
        },

        phone: {
          required: true,

        },
        address: {
          required: true,

        }
      },

      messages: {
        username: {
          required: errore_text.required,

        },
        email: {
          required: errore_text.required,
            email: errore_text.email
        },
        phone: {
          required: errore_text.required,
        },
        address: {
          required: errore_text.required,
        }
      },
ignore: ".ignore",
      submitHandler: function(form) {
        form.submit();
      }
    });
  }
}
