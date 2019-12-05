$(document).ready(function() {



  $('input[name="phone"]').mask('00/00/0000');


  $('.field-tickets_input input').click(function() {
    $('.field-tickets_input').parents('.input-tickets__box-contact').children('.input-tickets__grops').removeClass('input-tickets__grops-error');
  });


  if ($('input[type="tel"]').length > 0) {
    $('input[type="tel"]').mask("+380(99)999-99-99");
  }


  if ($('input[name="phone"]').length > 0) {
    $('input[name="phone"]').mask("+380(99)999-99-99");
  }




  // **************
  // active tabs
  // ****************
if (document.getElementsByClassName('tab__box').length > 0) {
  if (sessionStorage.buton_send_hero_form === 'send') {
        sessionStorage.tabs_items = document.querySelector('[data-value="' + sessionStorage.direction_hero_form + '"]').id
  }else {
    if (sessionStorage.buton_send_hero_form === 'send_menu') {
          sessionStorage.tabs_items = document.querySelector('[data-value="' + sessionStorage.direction_hero_form + '"]').id
          sessionStorage.buton_send_hero_form ='';
    }else {
      if (sessionStorage.tabs_items !== undefined) {
      } else {
          sessionStorage.tabs_items = document.getElementsByClassName('tab__item')[0].id
      }
    }

  }

}

  if (document.getElementsByClassName('tab__box').length > 0) {
    if (sessionStorage.buton_send_hero_form === 'send') {
      tabevent('tab__box', 'tab__item', sessionStorage.tabs_items, sessionStorage.cites_arrival, sessionStorage.cites_departure, sessionStorage.date);
    } else {
      tabevent('tab__box', 'tab__item', sessionStorage.tabs_items);
    }

  }

  function tabevent(box, item, tab_active_id, cites_arrival = false, cites_departure = false, date = false) {
    var info_tabs = null;
    info_tabs = {
      tabcontent: box,
      tablinks: item,
      tab_active: tab_active_id,
    }

    var tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(info_tabs.tabcontent);
    tablinks = document.getElementsByClassName(info_tabs.tablinks);

    active_tabs(tablinks, tabcontent, info_tabs.tab_active, cites_arrival, cites_departure, date);



    forEach(tablinks, function(index, value) {
      value.onclick = function(event) {
        sessionStorage.tabs_items = value.id;
        active_tabs(tablinks, tabcontent, event.target.id);
      };
    });
    // change_pluse();
  }


  // ***********
  // step2
  // **********


  function active_tabs(tablinks, tabcontent, tab_id_active, cites_arrival = false, cites_departure = false, date = false) {

    forEach(tablinks, function(index, value) {
      value.classList.remove('tab__item-active');
    });
    forEach(tabcontent, function(index, value) {
      value.classList.remove('tab__box-active');
    });

    var tabLinksactive, tabBoxContent;
// console.log(tab_id_active);
    tabLinksactive = document.getElementById(tab_id_active);
    console.log(tabLinksactive);
    tabLinksactive.classList.add('tab__item-active');

    tabBoxContent = document.querySelector('[data-tab="' + tab_id_active + '"]');
    tabBoxContent.classList.add('tab__box-active');

    if (tab_id_active == 'trip4') {
      $('.tickets__section_bus').addClass('tickets__section_bus-hover');
      $('.tickets__section_img-bus').removeClass('tickets__section_img-bus-hover');
      $('.tickets__section_img-evrop').addClass('tickets__section_img-evrop-hover');
    } else if (tab_id_active == 'trip3') {
      $('.tickets__section_bus').addClass('tickets__section_bus-hover');
      $('.tickets__section_img-evrop').removeClass('tickets__section_img-evrop-hover');
      $('.tickets__section_img-bus').addClass('tickets__section_img-bus-hover');
    } else {
      $('.tickets__section_img-evrop').addClass('tickets__section_img-evrop-hover');
      $('.tickets__section_img-bus').addClass('tickets__section_img-bus-hover');
      $('.tickets__section_bus').removeClass('tickets__section_bus-hover');
    }
    if (tabBoxContent.querySelectorAll('.input-tickets__box-sites .input-tickets__grops ').length > 0) {
      reservation_seat(tabBoxContent, tabBoxContent.dataset.value, cites_arrival, cites_departure, date);
      forEach(tabBoxContent.querySelectorAll('.input-tickets__box-sites .input-tickets__grops '), function(index, value) {
        value.classList.remove('input-tickets__grops-disabled');
      });
    }
  }


  function reservation_seat(element, direction_value, cites_arrival = false, cites_departure = false, date_hero_form = false, rerouting = false) {
    console.log(direction_value);
    var SITE_NAME = window.location.origin
    var order_info_url = SITE_NAME + '/set_params/';
    var data = {};
    $($(element).find('form').serializeArray()).each(function(index, obj) {
      data[obj.name] = obj.value;
    });
    console.log(data);
    if (sessionStorage.buton_send_hero_form === 'send') {
      data.arrival = cites_arrival;
      data.departion = cites_departure;
      data.date = date_hero_form;
    }
    data.direction = direction_value;
    $.ajax({
      url: order_info_url,
      type: 'POST',
      data: data,
      async: true,
      success: function(order) {
        $('.input-tickets__box-filds').find('.input-tickets__grops').addClass(' input-tickets__grops-disabled ');
        $('.tickets__disabled_seat').removeClass(' tickets__disabled_seat-active');
        $('.bus-seat').removeClass('bus-seat__active');
        $('.bus-seat').removeClass('bus-seat__disabled');
        $('.select__intup').find('.field_text').text(" ");
        $('.tickets_trip')[0].reset();
        $('.tickets_trip')[1].reset();
        $('.select__intup').find('input').attr('value', "");

        SKJ = order.order_sk
        // console.log(element);
        // console.log(cites_departure);
        data_update(element, '.data_departure', order.cities, false, cites_departure);
        data_update(element, '.data_arrival', order.cities, false, cites_arrival);
        // console.log(cites_departure);
        // console.log(cites_arrival);
        var data_order = order;

        resize_select_form_tiskets();
        console.log(rerouting);
        if (sessionStorage.buton_send_hero_form != 'send' && rerouting != true) {


          $('.input-tickets__box-filds').find('.input-tickets__grops').addClass(' input-tickets__grops-disabled ');
          $('.tickets__disabled_seat').removeClass(' tickets__disabled_seat-active');
          $('.bus-seat').removeClass('bus-seat__active');
          $('.bus-seat').removeClass('bus-seat__disabled');
          $('.select__intup').find('.field_text').text(" ");
          $('.tickets_trip')[0].reset();
          $('.tickets_trip')[1].reset();
          $('.select__intup').find('input').attr('value', "");

        }

        var wrap__box = element;

        var city__select__item = wrap__box.querySelectorAll('.input-tickets__box-sites .select__wrap_item');
        var city__select__input = wrap__box.querySelectorAll('.input-tickets__box-sites input');
        var datapicer = wrap__box.querySelector('.form__element_calendar');
        var datapicer_box = wrap__box.querySelector('.data_flights');
        var journey_time = wrap__box.querySelector('.flights__time');
        var payment_met = wrap__box.querySelector('.payment__method');
        var journey_time__wrap = journey_time.querySelector('.select__wrap');
        var datapicer_order;

        if (sessionStorage.buton_send_hero_form === 'send') {
          datapicer_order = $(datapicer).datepicker({
            minDate: new Date(),
            dateFormat: 'yyyy-mm-dd',
            autoClose: true,
            onRenderCell: function onRenderCell(date, cellType) {
              if (cellType == 'day') {
                if ($.inArray(formatDate(date), data_order.dates) < 0) {
                  return {
                    disabled: true
                  };
                }
              }
            },
            onHide: function onHide(dp, animationCompvared) {
              if (animationCompvared) {
                // ********************************
                //ajax data_flights start
                //*********************
                data.date = formatDate(dp.selectedDates)
                $.ajax({
                  url: order_info_url,
                  type: 'POST',
                  data: data,
                  async: true,
                  success: function(order) {
                    data_update(element, '.flights__time', order.times, true);
                    journey_time.classList.remove('input-tickets__grops-disabled');
                    clear_order();
                  }
                })
              }
            }
          }).data('datepicker');
          datapicer_order.selectDate(new Date(data.date));
          $.ajax({
            url: order_info_url,
            type: 'POST',
            data: data,
            async: true,
            success: function(order) {
              data_update(element, '.flights__time', order.times, true);
              journey_time.classList.remove('input-tickets__grops-disabled');
              clear_order();
            }
          })
          sessionStorage.removeItem('buton_send_hero_form')
          datapicer_box.classList.remove('input-tickets__grops-disabled');
        }

        if (rerouting == true) {
          forEach(city__select__item, function(index, value) {
            var city_json_value = $(city__select__input).serializeArray();
            if (city_json_value[0].value && city_json_value[1].value) {
              $('.form__element_calendar').val('');
              var datapicer_order = $(datapicer).datepicker({
                minDate: new Date(),
                dateFormat: 'yyyy-mm-dd',
                autoClose: true,
                onRenderCell: function onRenderCell(date, cellType) {
                  if (cellType == 'day') {
                    if ($.inArray(formatDate(date), data_order.dates) < 0) {
                      return {
                        disabled: true
                      };
                    }
                  }
                },
                onHide: function onHide(dp, animationCompvared) {
                  if (animationCompvared) {
                    // ********************************
                    //ajax data_flights start
                    //*********************
                    data.date = formatDate(dp.selectedDates)
                    $.ajax({
                      url: order_info_url,
                      type: 'POST',
                      data: data,
                      async: true,
                      success: function(order) {

                        data_update(element, '.flights__time', order.times, true);
                        journey_time.classList.remove('input-tickets__grops-disabled');
                        $('.tickets__disabled_seat').removeClass(' tickets__disabled_seat-active');
                        clear_order();
                      }
                    })
                  }
                }
              });
              datapicer_order.data('datepicker').clear();
              datapicer_box.classList.remove('input-tickets__grops-disabled');
            }
          });

          var box_input_tickets__box_sites = document.getElementsByClassName('tab__box-active')[0].querySelectorAll('.input-tickets__box-sites')[0].querySelectorAll('.input-tickets__grops');
          forEach(box_input_tickets__box_sites, function(index, value) {
            if (value.querySelectorAll('input')[0].value !== '') {
              console.log(value);
              console.log(box_input_tickets__box_sites[1].querySelectorAll('.select__wrap')[0].querySelectorAll(`[data-id="${value.querySelectorAll('input')[0].value}"]`)[0]);

              if (value.classList.contains('data_departure')) {
                box_input_tickets__box_sites[1].querySelectorAll('.select__wrap')[0].querySelectorAll(`[data-id="${value.querySelectorAll('input')[0].value}"]`)[0].classList.add('wwwwww-disabled');
              }
              if (value.classList.contains('data_arrival')) {
                box_input_tickets__box_sites[0].querySelectorAll('.select__wrap')[0].querySelectorAll(`[data-id="${value.querySelectorAll('input')[0].value}"]`)[0].classList.add('select__wrap_item-disabled');
              }
            }

          });
        }
        forEach(city__select__item, function(index, value) {
          $(value).on('click', function() {
            var city_json_value = $(city__select__input).serializeArray();
            if (city_json_value[0].value && city_json_value[1].value) {
              $('.form__element_calendar').val('');
              var datapicer_order = $(datapicer).datepicker({
                minDate: new Date(),
                dateFormat: 'yyyy-mm-dd',
                autoClose: true,
                onRenderCell: function onRenderCell(date, cellType) {
                  if (cellType == 'day') {
                    if ($.inArray(formatDate(date), data_order.dates) < 0) {
                      return {
                        disabled: true
                      };
                    }
                  }
                },
                onHide: function onHide(dp, animationCompvared) {
                  if (animationCompvared) {
                    // ********************************
                    //ajax data_flights start
                    //*********************
                    data.date = formatDate(dp.selectedDates)
                    $.ajax({
                      url: order_info_url,
                      type: 'POST',
                      data: data,
                      async: true,
                      success: function(order) {

                        data_update(element, '.flights__time', order.times, true);
                        journey_time.classList.remove('input-tickets__grops-disabled');
                        $('.tickets__disabled_seat').removeClass(' tickets__disabled_seat-active');
                        clear_order();
                      }
                    })
                  }
                }
              });
              datapicer_order.data('datepicker').clear();
              datapicer_box.classList.remove('input-tickets__grops-disabled');
            }
          });
        });
      }
    })
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


  function clear_order(name_select) {
    forEach(document.querySelectorAll('.seat-all__box'), function(index, value) {
      while ($(value)[0].firstChild) {
        $(value)[0].removeChild($(value)[0].firstChild);
      }
    });
    $('.seat-all_count').each(function() {
      $(this).text('0');
    });
    $('.input-tickets__box-filds').find('.booked_places').addClass(' input-tickets__grops-disabled ');
    $('.input-tickets__box-filds').find('.seat-box').addClass(' input-tickets__grops-disabled ');

    for (let i = 1; i < 22; i++) { // выведет 0, затем 1, затем 2
      var bus_item = document.querySelectorAll('[data-id="seat' + i + '"]');
      var bus_item_input = document.querySelectorAll('[name="seats"]');
      if (bus_item_input.length > 0) {
        forEach(bus_item_input, function(index, value) {
          value.remove();
        })
      }
      forEach(bus_item, function(index, value) {
        value.classList.remove('bus-seat__active');
        value.classList.remove('bus-seat__disabled');
      });
    }
  }


  function active_bus(wrap__box, test_masiv) {
    var data_all = {};
    $($(wrap__box).find('form').serializeArray()).each(function(index, obj) {
      data_all[obj.name] = obj.value;
    });
    var checkboxes = document.querySelectorAll('.seat-all__box')[0].getElementsByClassName('seat');
    var array = []
    for (var i = 0; i < checkboxes.length; i++) {
      array.push(checkboxes[i].dataset.item_s)
    }
    data_all.seats = array

    var SITE_NAME = window.location.origin
    var order_info_url = SITE_NAME + '/set_params/';

    $.ajax({
      url: order_info_url,
      type: 'POST',
      data: data_all,
      async: true,
      success: function(order) {
        console.log()
        // var sk_order = order.order_sk
        var bus_seats = order.seats_numbers;
        for (key in bus_seats) {
          bus_seats[+key + 1] = {
            value: bus_seats[+key + 1],
          }
        }
        for (key in order.seats_in_order) {
          bus_seats[order.seats_in_order[key].number].key_ssesions = order.seats_in_order[key].order_sk;
        }




        // var booked_places = doc.querySelector('.booked_places');
        // var booked_places = document.querySelector('.tab__box-active').querySelector('.booked_places')
        var bus_item_name;
        var tickets__disabled_seat = document.querySelectorAll('.tickets__disabled_seat');
        var seat_group = document.querySelector('.tab__box-active').querySelectorAll('.seat-group');
        var payment_met = document.querySelector('.tab__box-active').querySelector('.payment__method');

        for (var bus_seat in bus_seats) {
          var bus_item = document.querySelectorAll('[data-id="seat' + bus_seat + '"]');
          forEach(bus_item, function(index, value) {
            value.dataset.item = bus_seat;
            value.classList.add('bus-seat');
          });

          if (bus_seat < 10) {
            bus_item_name = '0' + bus_seat;
          } else {
            bus_item_name = bus_seat;
          }

          ;
          var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
          rect.setAttributeNS(null, 'x', 0.5);
          rect.setAttributeNS(null, 'y', 0.5);
          rect.setAttributeNS(null, 'rx', 4.5);
          rect.setAttributeNS(null, 'height', '69');
          rect.setAttributeNS(null, 'width', '69');
          rect.setAttributeNS(null, 'fill', '#20BF55');
          rect.setAttributeNS(null, 'stroke', 'none');
          forEach(bus_item, function(index, value) {
            value.appendChild(rect.cloneNode(true));
          });
          var text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          text.setAttributeNS(null, 'transform', 'translate(43 46)   rotate(-90)');
          text.innerHTML = bus_item_name;
          forEach(bus_item, function(index, value) {
            value.appendChild(text.cloneNode(true));
          });
          var devare_use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
          devare_use.setAttributeNS(null, 'href', '#Ellipse_13');
          devare_use.setAttributeNS(null, 'viewBox', '0 0 70 70');
          devare_use.setAttributeNS(null, 'x', 0);
          devare_use.setAttributeNS(null, 'y', 0);
          forEach(bus_item, function(index, value) {
            value.appendChild(devare_use.cloneNode(true));
          });

          if (typeof bus_seats[bus_seat].key_ssesions === "undefined") {

          } else if (bus_seats[bus_seat].key_ssesions === order.order_sk) {
            forEach(bus_item, function(index, value) {
              value.classList.add('bus-seat__active');
            });
          } else {
            forEach(bus_item, function(index, value) {
              value.classList.add('bus-seat__disabled');

            });
          }
        }

        // booked_places.classList.remove('input-tickets__grops-disabled');
        forEach(tickets__disabled_seat, function(index, value) {
          value.classList.add('tickets__disabled_seat-active');
        });
        forEach(seat_group, function(index, value) {
          value.classList.remove('input-tickets__grops-disabled');
        });
        payment_met.classList.remove('input-tickets__grops-disabled');
      }
    })

    // ********************************
    //ajax Для знаходження мість у бусі
    //*********************

  }


  $('.bus-seat').on('click', function() {
    var bus_seat_item = $(this).data('item');
    var box_input_seat = document.querySelectorAll('.input-tickets__main-seat');
    var seat_all__box = document.querySelectorAll('.seat-all__box');

    if ($(this).hasClass('bus-seat__disabled')) {
      return false;
    } else if ($(this).hasClass('bus-seat__active')) {
      $(this).removeClass('bus-seat__active');
      var box_input_seat = $('.seat-all__box');
      namber_item = $(this).data('item');
      forEach(document.querySelectorAll('[data-item_s="' + namber_item + '"]'), function(index, value) {
        value.remove();
      });
      forEach(document.getElementsByClassName('seat-all_count'), function(index, value) {
        value.innerText = box_input_seat[0].childElementCount;
      });

      if (box_input_seat[0].childElementCount < 7) {
        forEach(seat_all__box, function(index, value) {
          value.classList.remove('seat-all__box-small');
        });
      }
      forEach(document.querySelectorAll('.tab__box-active form')[0].querySelectorAll('.seat_bus_input'), function(index, value) {
        if (value.value == bus_seat_item) {
          value.remove();
        }
      });



    } else {

      $(this).addClass('bus-seat__active');
      var seat_bus = document.createElement('div');
      seat_bus.classList.add('seat');
      seat_bus.dataset.item_s = bus_seat_item;
      var seat_bus_input = document.createElement('input');
      seat_bus_input.setAttribute("type", "hidden");
      seat_bus_input.classList.add('seat_bus_input');
      seat_bus_input.setAttribute("name", 'seats');
      seat_bus_input.setAttribute("value", bus_seat_item);
      $(document.getElementsByClassName('tab__box-active')).find('form').append(seat_bus_input);

      var seat_item_texy = document.createElement('div');
      seat_item_texy.classList.add('seat-text');
      seat_item_texy.innerText = 'Место';
      var seat_item_count = document.createElement('div');
      seat_item_count.classList.add('seat-count');
      seat_item_count.innerText = bus_seat_item;
      var delevare_seat_bus = document.createElement('div');
      delevare_seat_bus.classList.add('seat_close');
      seat_bus.appendChild(seat_item_texy);
      seat_bus.appendChild(seat_item_count);
      seat_bus.appendChild(delevare_seat_bus);
      forEach(seat_all__box, function(index, value) {
        value.append(seat_bus.cloneNode(true));
      });

      forEach(document.querySelectorAll('.seat-all_count'), function(index, value) {
        value.innerText = box_input_seat[0].children[0].childElementCount;
      });

      if (box_input_seat[0].children[0].childElementCount > 6) {
        forEach(seat_all__box, function(index, value) {
          value.classList.add('seat-all__box-small');
        });
      }

      devare_seat_item();
    }


    // active_bus(document.getElementsByClassName('tab__box-active'));


  });


  $('.tickets__chesk_seat ').on('click', function() {
    var SITE_NAME = window.location.origin
    var order_info_url = SITE_NAME + '/set_params/';
    var get_seats_info_url = SITE_NAME + '/get_seats/';
    var data = {},
      array_sites = [];
    console.log($($(document.getElementsByClassName('tab__box-active')).find('form').serializeArray()));
    $($(document.getElementsByClassName('tab__box-active')).find('form').serializeArray()).each(function(index, obj) {
      data[obj.name] = obj.value;
      if (obj.name == "seats") {
        array_sites.push(obj.value);
        data[obj.name] = array_sites;
      }
    });

    $.ajax({
      url: get_seats_info_url,
      type: 'GET',
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

              var order_not_chesk = [];
              array_sites.forEach(function(item, i) {
                if (bus_seats_chesk[item].key_ssesions !== undefined && bus_seats_chesk[item].key_ssesions !== order.order_sk) {
                  order_not_chesk.push(item)
                }
              });

              if (order_not_chesk.length > 0) {
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





              } else {
                $('.check_seat__wrap').text(gettext('Всі ваші місця доступні для бронювання!'));
              }

            }
          }
        })
      }
    })
  });


  function devare_seat_item() {
    $('.seat_close').on('click', function(e) {
      if (e.target !== this) return;
      var box_input_seat = $('.seat-all__box');
      var imen_sear = $(this).parent().data('item_s');
      var seat_all__box = document.querySelectorAll('.seat-all__box'); // $(this).parent().remove();

      forEach(document.querySelectorAll('[data-item_s="' + imen_sear + '"]'), function(index, value) {
        value.remove();
      });
      forEach(document.getElementsByClassName('seat-all_count'), function(index, value) {
        value.innerText = box_input_seat[0].childElementCount;
      });
      forEach(document.querySelectorAll('[data-id="seat' + imen_sear + '"]'), function(index, value) {
        value.classList.remove('bus-seat__active');
      });

      if (box_input_seat[0].childElementCount < 7) {
        forEach(seat_all__box, function(index, value) {
          value.classList.remove('seat-all__box-small');
        });
      }
    });
  }
  pay_tisket();



  $('.rerouting_icon').on('click', function() {
    var tabactiveBoxContent = document.querySelector('.tab__box-active');
    var tab_item_rerouting = document.querySelector('.tab__item-active');

    var tab_rerouting = tabactiveBoxContent.dataset.value;

    var tab_item_rerouting_value = tab_item_rerouting.dataset.value;
    var tab_item_rerouting_name = tab_item_rerouting.dataset.name;

    var tab_item_rerouting_value_rout = tab_item_rerouting.dataset.value_rout;
    var tab_item_rerouting_name_rout = tab_item_rerouting.dataset.name_rout;

    var sitis_select = tabactiveBoxContent.querySelectorAll('.input-tickets__box-sites .input-tickets__grops .field');
    var city__select__input = tabactiveBoxContent.querySelectorAll('.input-tickets__box-sites input');
    var sitis_json_value = $(city__select__input).serializeArray();
    var city_departion_rerouting, city_arrival_rerouting;

    sitis_json_value.forEach(function(item, i) {
      if (item['name'] == "arrival") {
        city_departion_rerouting = item['value'];
      }
      if (item['name'] == "departion") {
        city_arrival_rerouting = item['value'];
      }
    });

    tab_item_rerouting.dataset.value = tab_item_rerouting_value_rout;
    tabactiveBoxContent.dataset.value = tab_item_rerouting_value_rout;

    tab_item_rerouting.innerText = tab_item_rerouting_name_rout;
    tab_item_rerouting.dataset.value_rout = tab_item_rerouting_value;

    tab_item_rerouting.dataset.name = tab_item_rerouting.dataset.name_rout;
    tab_item_rerouting.dataset.name_rout = tab_item_rerouting_name;

    var tabcontent = document.getElementsByClassName('tab__box');
    var tablinks = document.getElementsByClassName('tab__item');
    reservation_seat(tabactiveBoxContent, tab_item_rerouting_value_rout, city_arrival_rerouting, city_departion_rerouting, false, true);



  })

  function resize_select_form_tiskets() {
    if (document.documentElement.clientWidth < 781) {
      var steps = $('.tab__box-active').find(".input-tickets__box");
      var count = steps.length;

      steps.each(function(i) {
        var page_step = i + 1;

        if (i == 0) {
          $('.tab__box-active').find("#step" + i).show();
        } else {
          $('.tab__box-active').find("#step" + i).hide();
        }

        if ($(this).parent('.fieldset__box').hasClass('fieldset__box') !== true) {
          $(this).wrap("<div class='fieldset__box' id='step" + i + "'></div>");

          if (i == 0) {

            createNextButton(i); // to do

            $('.tab__box-active').find("#step" + i).show();
          } else {
            $('.tab__box-active').find("#step" + i).hide();
            createPrevButton(i); // to do

            createNextButton(i); // to do
          }
        }
      });
    }
  }


  function createPrevButton(i) {
    var stepName = "step" + i;

    if (i > 0) {
      $('.tab__box-active').find("#" + stepName + ' .input-tickets__box_contros').append("<a href='#' id='" + stepName + "Prev' class='prev_tite prev_step btn btn-greyy'><i class='fas fa-angle-left'></i> </a>");
    }

    $('.tab__box-active').find("#" + stepName + "Prev").bind("click", function(e) {
      $('.tab__box-active').find("#" + stepName).hide();
      $('.tab__box-active').find("#step" + (i - 1)).show();
    });
  }


  $("#order_tiskets").on('click', function() {
    if (document.documentElement.clientWidth < 781) {
      console.log("crash");
      location.href = "/order/";
    }
  })

})

function createNextButton(i) {
  var stepName = "step" + i;

  if (i == 0) {
    $('.tab__box-active').find("#" + stepName + ' .input-tickets__box_contros').append("<a href='#' id='" + stepName + "Next' class='next_tite btn btn-blue'>Выбрать дату и рейс  </a>");
  } else if (i == 1) {
    $('.tab__box-active').find("#" + stepName + ' .input-tickets__box_contros').append("<a href='#' id='" + stepName + "Next' class='next_tite btn btn-blue'>Выбрать место  </a>");
  } else if (i == 2) {
    $('.tab__box-active').find("#" + stepName + ' .input-tickets__box_contros').append("<a href='#' id='" + stepName + "Next' class='next_tite btn btn-blue'>Оформить билет </a>");
  } else if (i == 3) {
    $('.tab__box-active').find("#" + stepName + ' .input-tickets__box_contros ').append("<a href='#' class=' pay_tisket  next_tite btn btn-blue'>Перейти к оплате </a>");
      pay_tisket();
  }

  $('.tab__box-active').find("#" + stepName + "Next").bind("click", function(e) {
    var flag = true;
    $.each($('.tab__box-active').find("#" + stepName + ' input'), function(index, input) {
      if ($(input).val().trim() === "") {
        flag = false;
        $(input).parents('.input-tickets__grops').addClass('input-tickets__grops-error');
      }
    });

    if (flag !== false) {
      $('.tab__box-active').find("#" + stepName).hide();
      $('.tab__box-active').find("#step" + (i + 1)).show();
    }
  });
}
function pay_tisket() {
  $('.pay_tisket').on('click', function() {
    event.preventDefault();

    check_seat_buss();
  });
}



function check_seat_buss() {
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
  var flag_error = 0;
  var array_sites = [];
  forEach(inputs, function(index, value) {
    if ($(value).val()) {} else {
      flag_error++;
      console.log(value);
      $(value).parents('.input-tickets__grops').addClass('input-tickets__grops-error');
    }
  });


  if (flag_error === 0) {


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
          $(document.getElementsByClassName('tab__box-active')).find('form').submit()
        }

      }
    })

  }
}
