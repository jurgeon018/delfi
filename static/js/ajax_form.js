$(function() {

  Onload();
})

function Onload() {
 
if(document.getElementById('#tickets_ewrop_info')){
  valide_form('#tickets_ewrop_info','.input-tickets__grops', '/create_europe_order/');
}

if(document.getElementById('#bus_bus_order')){
  valide_form('#bus_bus_order','.input-tickets__grops','/create_bus_order/');
}

if(document.getElementById('#form_contact_form')){
  valide_form('#form_contact_form','.input-tickets__grops','/form_contact_bus/');
}



}

function location_leng() {
  return location.pathname.split('/')[1];
}

function valide_form(id_form, append_error_box,url_form ) {
  console.log(url_form_tab);
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
function form_ajax_static(id_form,url_form){


  var form_input, form_json={},url_form;
  var SITE_NAME = window.location.origin
  var url_form = SITE_NAME + url_form;
  form_input = $(id_form).serializeArray();
  var flag_chesk = 0;
  $(form_input).each(function(index, obj) {
    form_json[obj.name] = obj.value;

  });
console.log(url_form);
console.log(form_input);
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
//   $.ajax({
//     url: url_form,
//     type: 'POST',
//     data:form_input,
//     async: true,
//     success: function(order) {
// console.log(order);
//
//
//     }
//   })


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
