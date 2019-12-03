  function hero_form(element) {
    if (element.length > 0) {
      var SITE_NAME = window.location.origin
      var order_info_url = SITE_NAME + '/set_params/';
      var data_hero_form = {
        direction: element[0].dataset.value
      };
      var wrap_element = element[0];
      var datapicer_hero = element[0].querySelector('.form__element_calendar_hero');
      var isCalendarVisible = false;
      $.ajax({
        url: order_info_url,
        type: 'POST',
        data: data_hero_form,
        async: true,
        success: function(order) {
          data_update(wrap_element, '.cites_departure', order.cities, false);
          data_update(wrap_element, '.cites_arrival', order.cities, false);
          var heroFormDatepicker = $(datapicer_hero).datepicker({
            minDate: new Date(),
            dateFormat: 'yyyy-mm-dd',
            autoClose: true,
            onRenderCell: function onRenderCell(date, cellType) {
              if (cellType == 'day') {
                if ($.inArray(formatDate(date), order.dates) < 0) {
                  return {
                    disabled: true
                  };
                }
              }
            }
          });
          $(element[0].querySelector('.datepicker_icon')).on('click', function(event) {
            var heroFormDatepicker = $(datapicer_hero).data('datepicker');
            if ($(datapicer_hero).datepicker("widget").is(":visible")) {
              $(datapicer_hero).datepicker("hide");
            } else {
              $(datapicer_hero).datepicker("show");
            }
          });
        }
      })
      $(element[0].querySelector('.datepicker_icon')).on('click', function(event) {
        var heroFormDatepicker = $(datapicer_hero).data('datepicker');
        if ($(heroFormDatepicker.$datepicker)[0].classList.contains('active') === true) {
          heroFormDatepicker.hide();
        } else {
          heroFormDatepicker.show();
        }
      });

      $(element[0].querySelector('.btn-hero-form')).on('click', function(event) {
        event.preventDefault();
        var hero_form_serialize = $(element[0].querySelector('form')).serializeArray();
        for (var key in hero_form_serialize) {
          if (hero_form_serialize[key].value == false) {
            element[0].querySelector('form').querySelector('.' + hero_form_serialize[key].name).classList.add("form__group_error");
          } else {
            if (window.sessionStorage) {
              for (var key in hero_form_serialize) {
                if (hero_form_serialize.hasOwnProperty(key)) {
                  sessionStorage.setItem(hero_form_serialize[key].name, hero_form_serialize[key].value);
                }
                sessionStorage.setItem('direction_hero_form', element[0].dataset.value);
              }
            }
          }
          if (hero_form_serialize[0].value != false && hero_form_serialize[1].value != false && hero_form_serialize[2].value != false) {
            sessionStorage.setItem('buton_send_hero_form', 'send');
            location.href = "/order/"
          }
        }
      })



    }
  }
  function data_update(parent_box, name_select, params, flag_ajax, active_element = false) {

    var select_box = parent_box.querySelector(name_select);
    var select_wrap = select_box.querySelector('.select__wrap');
    var fragment = document.createDocumentFragment();
    for (var key in params) {
      var select__item = document.createElement('div');
      select__item.classList.add('select__wrap_item');
      select__item.dataset.id = params[key];
      select__item.innerHTML = params[key];



      if (params[key] == active_element) {
        console.log($(select_wrap).parents('.input-tickets__grops'));
        $(select_wrap).siblings(".field").children('.field_text').each(function() {
          var paragraph = $(this).text(params[key]);
        });
        select__item.classList.add('select__wrap_item');
        $(select_wrap).siblings(".field").children('input').each(function() {
          $(this).val(params[key]);
        });
      }
      fragment.appendChild(select__item);
    }

    while ($(select_wrap)[0].firstChild) {
      $(select_wrap)[0].removeChild($(select_wrap)[0].firstChild);
    }
    if (name_select === '.flights__time') {

      $(select_wrap).siblings(".field").children('.field_text').each(function() {
        $(this).text('');
      });
      $(select_wrap).siblings(".field").children('input').each(function() {
        $(this).val('');
      });


    }
    $(select_wrap)[0].appendChild(fragment);

    // journey_time.classList.remove('input-tickets__grops-disabled'); //************* Привязка кода до  створеного списку рейсів
    if (flag_ajax === true) {
      forEach(select_wrap.querySelectorAll('.select__wrap_item'), function(index, value) {
        $(value).on('click', function() {

          if (!$(this).hasClass('select__wrap_item-disabled')) {



            if ($(this).parents('.input-tickets__box-sites').length > 0) {
              forEach($(this).parents('.input-tickets__box-sites').find('.data_arrival').find('.select__wrap .select__wrap_item'), function(index, value) {
                value.classList.remove('select__wrap_item-disabled');
              });

              // $(this).parents('.input-tickets__box-sites').find('.data_arrival').find('.select__wrap').each()
              if ($(this).parents('.input-tickets__grops').hasClass('data_departure')) {
                $(this).parents('.input-tickets__box-sites').find('.data_arrival').find('.select__wrap').find(`[data-id="${$(this).data('id')}"]`).addClass('select__wrap_item-disabled');
              }
            }
            if ($(this).parents('.input-tickets__box-sites').length > 0) {
              forEach($(this).parents('.input-tickets__box-sites').find('.data_departure').find('.select__wrap .select__wrap_item'), function(index, value) {
                value.classList.remove('select__wrap_item-disabled');
              });
              if ($(this).parents('.input-tickets__grops').hasClass('data_arrival')) {
                $(this).parents('.input-tickets__box-sites').find('.data_departure').find('.select__wrap').find(`[data-id="${$(this).data('id')}"]`).addClass('select__wrap_item-disabled');
              }
            }
            var text = $(this).text();
            var id = $(this).data('id');
            var field = $(this).parents('.select').find(".field_text ");
            var input_select = $(this).parents('.select').find("input");
            $(field).text(text);
            $(input_select).val(id);
            $('.select__wrap').removeClass('select__wrap-active');
            $('.field').removeClass('field-active');
          }


          active_bus(parent_box);
          clear_order(name_select);
        });
      });

    } else {
      $('.select__wrap_item').on('click', function() {

        if (!$(this).hasClass('select__wrap_item-disabled')) {
          if ($(this).parents('.input-tickets__box-sites').length > 0) {
            forEach($(this).parents('.input-tickets__box-sites').find('.data_arrival').find('.select__wrap .select__wrap_item'), function(index, value) {
              value.classList.remove('select__wrap_item-disabled');
            });

            // $(this).parents('.input-tickets__box-sites').find('.data_arrival').find('.select__wrap').each()
            if ($(this).parents('.input-tickets__grops').hasClass('data_departure')) {
              $(this).parents('.input-tickets__box-sites').find('.data_arrival').find('.select__wrap').find(`[data-id="${$(this).data('id')}"]`).addClass('select__wrap_item-disabled');
            }
          }
          if ($(this).parents('.input-tickets__box-sites').length > 0) {
            forEach($(this).parents('.input-tickets__box-sites').find('.data_departure').find('.select__wrap .select__wrap_item'), function(index, value) {
              value.classList.remove('select__wrap_item-disabled');
            });
            if ($(this).parents('.input-tickets__grops').hasClass('data_arrival')) {
              $(this).parents('.input-tickets__box-sites').find('.data_departure').find('.select__wrap').find(`[data-id="${$(this).data('id')}"]`).addClass('select__wrap_item-disabled');
            }
          }
          var text = $(this).text();
          var id = $(this).data('id');
          var field = $(this).parents('.select').find(".field_text ");
          var input_select = $(this).parents('.select').find("input");
          $(field).text(text);
          $(input_select).val(id);
          $('.select__wrap').removeClass('select__wrap-active');
          $('.field').removeClass('field-active');
        }
      });
    }
  }
  function formatDate(date) {
    var d = new Date(date),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate(),
      year = d.getFullYear();
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    return [year, month, day].join('-');
  }
  var forEach = function forEach(array, callback, scope) {
    for (var i = 0; i < array.length; i++) {
      callback.call(scope, i, array[i]); // passes back stuff we need
    }
  };


function _defineProperty(obj, key, value) {
  if (key in obj) {
    Object.defineProperty(obj, key, {
      value: value,
      enumerable: true,
      configurable: true,
      writable: true
    });
  } else {
    obj[key] = value;
  }
  return obj;
}
// const imageObserver = new IntersectionObserver((entries, imgObserver) => {
//            entries.forEach((entry) => {
//                if (entry.isIntersecting) {
//                    const lazyImage = entry.target
//                    console.log("lazy loading ", lazyImage);
//                    lazyImage.src = lazyImage.dataset.src
//                    lazyImage.classList.remove("lzy_img");
//                    imgObserver.unobserve(lazyImage);
//                }
//            })
//        });
//        const arr = document.querySelectorAll('.b-lazy')
//        arr.forEach((v) => {
//
//            imageObserver.observe(v);
//    })
console.log("crash");
$(document).ready(function() {
  var _$$slick;
  var bLazy = new Blazy({
    offset: 100 // Loads images 100px before they're visible
  });

  hero_form(document.getElementsByClassName('hero__form'));

  $('.btn_directions_dk').on('click',function(){
    event.preventDefault();
    sessionStorage.buton_send_hero_form = 'send';
    sessionStorage.direction_hero_form = 'dk';
    location.href="/order/";
  })
  $('.btn_directions_dl').on('click',function(){
    event.preventDefault();
    sessionStorage.buton_send_hero_form = 'send';
    sessionStorage.direction_hero_form = 'kl';
    location.href="/order/";
  })
  $('.btn_directions_europe').on('click',function(){
    event.preventDefault();
    sessionStorage.buton_send_hero_form = 'send';
    sessionStorage.direction_hero_form = 'europe';
    location.href="/order/";
  })
  $('.btn_directions_bus_order').on('click',function(){
    event.preventDefault();
    sessionStorage.buton_send_hero_form = 'send';
    sessionStorage.direction_hero_form = 'bus_order';
    location.href="/order/";
  })


  $('.btn_more_park').on('click', function() {
    event.preventDefault();
    $('html,body').animate({scrollTop:$('#bus-slider_wrap').offset().top+"px"},{duration:1E3});
  });


  $('.btn-license').on('click', function() {
    event.preventDefault();
    $('html,body').animate({scrollTop:$('.license_block').offset().top+"px"},{duration:1E3});
  });

  $(".scroll_our-servise").click(function() {
    $([document.documentElement, document.body]).animate({
      scrollTop: $("#our-servise").offset().top
    }, 500);
  });
  $('.info-car-park__button_link').fancybox({
    openEffect: 'none',
    closeEffect: 'none',
    helpers: {
      media: {}
    }
  });
  change_pluse();
  function change_pluse() {
    $('.input__pl-min_minus').click(function() {
      var $input = $(this).parent().find('input');
      var count = parseInt($input.val()) - 1;
      count = count < 1 ? 1 : count;
      $input.val(count);
      $input.change();
      return false;
    });
    $('.input__pl-min_plus').click(function() {
      var $input = $(this).parent().find('input');
      $input.val(parseInt($input.val()) + 1);
      $input.change();
      return false;
    });
  }
  $('.input__pl-min_faild').on("keyup",function(ev){
    var $input = $(this).parent().find('input');
    var input_value = parseInt($input.val());

    if (isNaN(input_value)) {
      input_value = 0;
    }
    $input.val(input_value );

    return false;
});

  $('.tickets__seat_help').on('click', function() {
    $('.tickets__description').toggleClass('tickets__description-active');
    $('.tickets__disabled_seat').toggleClass('tickets__disabled_seat-description-active');
    $(document).mouseup(function(e) {
      // событие клика по веб-документу
      var div = $(".tickets__description"); // тут указываем класс элемента

      if (!div.is(e.target) // если клик был не по нашему блоку
        &&
        div.has(e.target).length === 0) {
        // и не по его дочерним элементам
        $('.tickets__description').removeClass('tickets__description-active');
        $('.tickets__disabled_seat').removeClass('tickets__disabled_seat-description-active');
      }
    });
  });
  $('.tickets__description-close').on('click', function() {
    $('.tickets__description').removeClass('tickets__description-active');
    $('.tickets__disabled_seat').removeClass('tickets__disabled_seat-description-active');
  });
  $(".card").mouseover(function(e) {
    $(this).addClass("cart-hover");
  });
  $(".card").mouseout(function(e) {
    $(this).removeClass("cart-hover");
  });
  $(".js-hamburger").on('click', function(e) {
    $('.js-hamburger').toggleClass('is-active');
    $('.fix-box__main ').toggleClass('fix-box__main-active');
  });
  $('.nav__menu_item-drop').on('click', function(e) {
    e.preventDefault();
    $('.nav__menu_sub').toggleClass('main-menu__sub-active');
  });

  function hasClass(element, className) {
    return element.className && new RegExp("(^|\\s)" + className + "(\\s|$)").test(element.className);
  }

  function doSomething() {
    if ($(this).parents(".input-tickets__grops-disabled").length) {
      return false;
    } else {

      forEach($(this).parents('.form__wrap').children('.form__group'), function(index, value) {
        value.classList.remove('form__group_error');
      });


      var select__wrap = $(this).parent('.select').find(".select__wrap");
      var field = $(this).parent('.select').find(".field");

      if (hasClass(select__wrap[0], 'select__wrap-active')) {
        $(select__wrap).toggleClass('select__wrap-active');
        $(field).toggleClass('field-active');
      } else {
        $('.select__wrap').removeClass('select__wrap-active');
        $('.field').removeClass('field-active');
        $(select__wrap).addClass('select__wrap-active');
        $(field).addClass('field-active');
      }
    }


    $(document).mouseup(function(e) {
      // событие клика по веб-документу
      var div = $(this).parent('.select').find(".select__wrap"); // тут указываем класс элемента

      if (!div.is(e.target) // если клик был не по нашему блоку
        &&
        div.has(e.target).length === 0) {
        // и не по его дочерним элементам
        $('.select__wrap').removeClass('select__wrap-active');
        $('.field').removeClass('field-active');
      }
    });
  }

  $('.select__intup').on('click', doSomething);
  select__wrap_item();
  $(".our-servise__wrap").slick({
    dots: false,
    infinite: false,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 1,
    responsive: [{
      breakpoint: 1055,
      settings: {
        slidesToShow: 3,
        dots: true,
        slidesToScroll: 1
      }
    }, {
      breakpoint: 692,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        dots: true
      }
    }, {
      breakpoint: 465,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        variableWidth: true,
        dots: true
      }
    }]
  });
  $(".customer-reviews__wrap").slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 1,
    nextArrow: '.customer-reviews_next',
    prevArrow: '.customer-reviews_prew',
    responsive: [{
      breakpoint: 1070,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    }, {
      breakpoint: 1500,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    }, {
      breakpoint: 665,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }]
  }); // forEach method, could be shipped as part of an Object Literal/Module start

  var forEach = function forEach(array, callback, scope) {
    for (var i = 0; i < array.length; i++) {
      callback.call(scope, i, array[i]); // passes back stuff we need
    }
  }; // select tiskey style hover


  var tisket_select = document.querySelectorAll('.input-tickets__grops:not(.input-tickets__grops-disabled) .input-tickets__main .select-tickets .select__intup ');

  function hover_field(tisket_select) {
    if (tisket_select) {
      forEach(tisket_select, function(index, value) {
        value.onmouseleave = function(event) {
          value.classList.remove('select-tickets-active');
        };

        value.onmouseenter = function(event) {
          value.classList.add('select-tickets-active');
        };
      });
    }
  }

  hover_field(tisket_select);
  hover_field(document.querySelectorAll('.input-tickets__main')); // tabs contant






  hover_class('seat-all', 'seat-all__wrap-active');
  $(".tickets__control_step-next").on('click', function() {














      data_all = {};
      $($(document.getElementsByClassName('tab__box-active')).find('form').serializeArray()).each(function(index, obj) {
        data_all[obj.name] = obj.value;
      });

      var checkboxes = document.querySelectorAll('.seat-all__box')[0].getElementsByClassName('seat');
      var array = [];
      for (var i = 0; i < checkboxes.length; i++) {
        array.push(checkboxes[i].dataset.item_s)
      }
      data_all.seats = array
      console.log(data_all)

      var SITE_NAME = window.location.origin
      var order_info_url = SITE_NAME + '/set_params/';
      var create_order = SITE_NAME + '/create_order/';
      var get_seats_info_url = SITE_NAME + '/get_seats/';
      var box_active_order = document.getElementsByClassName('tab__box-active')[0];
      var inputs = $(box_active_order).find('.input-tickets__box-contact').find('input');

      var array_sites = [];





        var SITE_NAME = window.location.origin
        var order_info_url = SITE_NAME + '/set_params/';
        var get_seats_info_url = SITE_NAME + '/get_seats/';
        var data = {},
          array_sites = [];
        // console.log($($(document.getElementsByClassName('tab__box-active')).find('form').serializeArray()));
        $($(document.getElementsByClassName('tab__box-active')).find('form').serializeArray()).each(function(index, obj) {
          data[obj.name] = obj.value;
          if (obj.name == "seats") {
            array_sites.push(obj.value);
            data[obj.name] = array_sites;
          }
        });

        $.ajax({
          url: get_seats_info_url,
          type: 'GEt',
          async: true,
          success: function(order) {


            var bus_seats_chesk = order.seats_numbers;
            for (key in bus_seats_chesk) {
              bus_seats_chesk[+key + 1] = {
                value: bus_seats_chesk[+key + 1],
              }
            }
            for (key in order.seats_in_order) {
              bus_seats_chesk[order.seats_in_order[key].number].key_ssesions = order.seats_in_order[key].order_sk;
            }

            var order_not_chesk = [];
            array_sites.forEach(function(item, i) {
              if (bus_seats_chesk[item].key_ssesions !== undefined && bus_seats_chesk[item].key_ssesions !== order.order_sk) {
                order_not_chesk.push(item)
              }
            });

            if (order_not_chesk.length > 0) {

            $.fancybox.open({
              src: '#chesk_form_bus',
              type: 'inline',
              touch: false,
              autoStart: false,
              padding: 0,
              hideOnClose: false,
              showCloseButton: true,
              opts: {
                afterShow: function(instance, current) {


                        var box_input_seat = $('.seat-all__box');
                    var seats_buss_chesk = 'Місце під номером: ';
                    order_not_chesk.forEach(function(item, i) {


                      var bus_item = document.querySelectorAll('[data-id="seat' + item + '"]');
                      forEach(bus_item, function(index, value) {
                        value.classList.add('bus-seat__disabled');
                        value.classList.remove('bus-seat__active');
                      });
                      forEach(document.querySelectorAll('[data-item_s="' + item + '"]'), function(index, value) {
                        value.remove();
                      });

                      forEach(document.querySelectorAll('.tab__box-active form')[0].querySelectorAll('.seat_bus_input'), function(index, value) {
                        if (value.value == item) {
                          value.remove();
                        }
                      });

                      forEach(document.getElementsByClassName('seat-all_count'), function(index, value) {
                        value.innerText = box_input_seat[0].childElementCount;
                      });


                      if (i == order_not_chesk.length - 1) {
                        seats_buss_chesk += item + ' ';

                      } else {
                        seats_buss_chesk += item + ', ';
                      }
                    });
                    $('.check_seat__wrap').text(seats_buss_chesk + ' зайняте');







                }
              }
            })
          } else {
            console.log("crash");
            var box_active_order = document.getElementsByClassName('tab__box-active')[0];
            var inputs = $(box_active_order).find('.tickets__box_seat').find('input');
            var flag_error = 0;
            forEach(inputs, function(index, value) {
              if ($(value).val()) {} else {
                flag_error++;
                $(value).parents('.input-tickets__grops').addClass('input-tickets__grops-error');

              }
            });
            var inputs_seats = $(box_active_order).find('.seat_bus_input');

            if (inputs_seats.length<1) {
              flag_error++;
              $.fancybox.open({
                src: '#error_search',
                type: 'inline',
                touch: false,
                autoStart: false,
                padding: 0,
                hideOnClose: true
              });


            }
            if (flag_error === 0) {
              $('.tickets__box_seat').removeClass('tickets__box_seat-active');
              $('.tickets__box_contact').addClass('tickets__box_contact-active');
            }
          }

          }
        })

  });
  if (document.getElementsByClassName('tickets_trip').length>0) {
    document.getElementsByClassName('tickets_trip')[0].onclick = function(e){
      $('.input-tickets__grops').removeClass('input-tickets__grops-error');
    }
  }



  $(".tickets__control_step-prev").on('click', function() {
    $('.tickets__box_seat').addClass('tickets__box_seat-active');
    $('.tickets__box_contact').removeClass('tickets__box_contact-active');
  }); // Формат дати для запису в календар

  function formatDate(date) {
    var d = new Date(date),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate(),
      year = d.getFullYear();
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    return [year, month, day].join('-');
  }

  function hover_class(element, addClass) {
    element = document.getElementsByClassName(element);

    if (element) {
      forEach(element, function(index, value) {
        value.onmouseleave = function(event) {
          value.classList.remove(addClass);
        };

        value.onmouseenter = function(event) {
          value.classList.add(addClass);
        };
      });
    }
  }

  function select__wrap_item() {
    $('.select__wrap_item').on('click', function() {
      // console.log("crash");
      var text = $(this).text();
      var id = $(this).data('id');
      var field = $(this).parents('.select').find(".field_text ");
      var input_select = $(this).parents('.select').find("input");
      $(field).text(text);
      $(input_select).val(id);
      $('.select__wrap').removeClass('select__wrap-active');
      $('.field').removeClass('field-active');
    });
  }

  $('.img_modal').on('click', function(event) {
    event.preventDefault();
    $.fancybox.open({
      src: this.href,
      type: 'image',
      Width: 660
    });
  });
  $(".license__wrap").slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 1,
    nextArrow: '.customer-reviews_next',
    prevArrow: '.customer-reviews_prew',
    responsive: [{
      breakpoint: 1100,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        // infinite: true,
        dots: false
      }
    }, {
      breakpoint: 850,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    }, {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }]
  });
  $(".bus-slider").slick((_$$slick = {
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    swipe: false,
    slidesToScroll: 1,
    // arrows: false,
    prevArrow: false
  }, _defineProperty(_$$slick, "dots", false), _defineProperty(_$$slick, "nextArrow", '.bus-slider-nexts'), _$$slick));
  $('div[data-slide]').click(function(e) {
    e.preventDefault();
    var slideno = $(this).data('slide');
    $('.bus-slider').slick('slickGoTo', slideno - 1);
  });
  $(".tabs-list-item").on("click", function(e) {
    e.preventDefault();

    $(this).parent().children(".tabs-list-item").removeClass("tabs-list-item-active");
    $(this).parents(".tabs").children(".tabs-content").removeClass("tabs-content-active");
    $(this).addClass("tabs-list-item-active");
    $($(this).attr("href")).addClass("tabs-content-active");

    var parent_block = $(this).parents('.bus-slider-item')[0];
    var id_active = $(this).attr("href");

    forEach($(this).parents(".tabs").children(".tabs-content"), function(index, value) {
      if (value.dataset.id == id_active) {
        value.classList.add('tabs-content-active')
      }
    })

    // console.log($(this));
    forEach(parent_block.getElementsByClassName('bus-slider_main_content'), function(index, value) {
      // // value.data('id');
      // value.classList.remove('bus-slider_main_content-hiden')
      value.classList.remove('bus-slider_main_content-active')
      if (value.dataset.id == id_active) {
        value.classList.add('bus-slider_main_content-active')
        if (value.dataset.id == '#two') {
          $(value).slick({
            dots: true,
            infinite: false,
            speed: 300,
            slidesToShow: 1,
            slidesToScroll: 1,
            centerMode: true,

            arrows: false,
            centerPadding: '20px',
            centerMargin: '0px',
            responsive: [{
              breakpoint: 768,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            },
            {
              breakpoint:380,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '0px',
              }
            },
          ]
          });

        }
      }



    });




    // $('[data-id="'+$(this).attr("href")+'"]').addClass("bus-slider_main_content-active");
  });


  $(".bus-card__item").on("click", function(e) {
    e.preventDefault();
    $(".bus-card__item").removeClass("bus-card__item-active");
    $(this).addClass("bus-card__item-active"); // $($(this).attr("href")).addClass("tabs-content-active");
  });
  $('.tickets__description_btn').on('click', function() {
    $.fancybox.open({
      src: '#calculate',
      type: 'inline',
      touch: false,
      autoStart: false,
      padding: 0,
      hideOnClose: true
    });
  });

  $('.btn_send_conditions').on('click', function() {
    $.fancybox.close();
  });
  $('.tickets__disabled-icon').on('click', function() {
    $.fancybox.open({
      src: '#tickets__disabled',
      type: 'inline',
      touch: false,
      autoStart: false,
      padding: 0,
      hideOnClose: true
    });
  });

});
