(function($) {

  // function post(plugin, args) {
  //   console.log("plugin")
  //   // console.log(plugin)
  //   // console.log("plugin")
  //   // htmlFormatting(args.node, {
  //   //   'h1': {
  //   //     convert_to: 'h2',
  //   //     valid_styles: '',
  //   //     valid_classes: '',
  //   //     no_empty: true,
  //   //     // valid_elements: headerRule,
  //   //     valid_elements: {
  //   //
  //   //       'span': {
  //   //         process: function (node) {
  //   //           console.log(node)
  //   //             var parent = node.parentNode
  //   //             space = document.createTextNode(' ');
  //   //             parent.replaceChild(space, node);
  //   //         }
  //   //       }
  //   //     },
  //   //   },
  //   // });
  // }

  {% if is_admin_inline %}
  $(function() {
    {% endif %}
    function tinymce4_init(selector) {
      var tinymce4_config = {
        {% for key, value in callbacks.items %}
          '{{ key }}': {{ value|safe }},
        {% endfor %}

        setup: function (editor) {
          editor.on('change', function () {
            editor.save();
          });
        },
        {{ tinymce_config|safe }}
      };

      if (typeof selector != 'undefined') {
        tinymce4_config['selector'] = selector;
      }
      console.log('tinymce_test');
      // tinymce4_config.paste_postprocess = post;
      tinymce4_config.paste_postprocess = function(plugin, args) {
        console.log("test123");
          // console.log(args.node);
          // args.node.setAttribute('id', '42');
      }

      tinymce.init(tinymce4_config);


    } // End tinymce4_init
{% if not is_admin_inline %}
    tinymce4_init();
})();
{% else %}
    // Add TinyMCE 4 widgets to textaras inside a node
    function add_editors(node) {

      $(node).find('.tinymce4-editor').each(function(i, elem) {
        console.log(i);
        if ($(elem).css('display') != 'none' && elem.id.indexOf('__prefix__') == -1) {
          tinymce4_init(elem.tagName + '#' + elem.id);
        }
      });
    }

    // Remove TinyMCE 4 widgets from textareas inside a node
    function remove_editors(node) {
      $(node).find('.tinymce4-editor').each(function(i, elem) {
        $(tinymce.EditorManager.editors).each(function(i, editor) {
          if (editor.id == elem.id) {
            editor.remove();
          }
        });
      });
    }

    // Restore consistency of TinyMCE 4 widgets
    function refresh_editors() {
      $(tinymce.EditorManager.editors).each(function(i, editor) {
        var elem = editor.getElement();
        if (editor.id != elem.id) {
          editor.remove();
          tinymce4_init(elem.tagName + '#' + elem.id);
        }
      });
    }

    // Use MutationObserver to track adding or removing Django admin inline formsets
    // to add adn remove TinyMCE editor widgets.
    var observer = new MutationObserver(function(mutations) {
      $(mutations).each(function(i, mutation) {
        $(mutation.addedNodes).each(function(i, node) {
          // Add TinyMCE widgets to new textareas.
          add_editors(node);
        }); // End addedNodes
        $(mutation.removedNodes).each(function(i, node) {
          // Remove TinyMCE widgets from textareas inside removed nodes.
          remove_editors(node);
          // Refresh remaining TinyMCE widgets to return them to consistent state
          // After removing an inline formset, Django admin scripts
          // change IDs of remaining textareas,
          // so textarea ID != ID of the TinyMCE instance attached to it.
          refresh_editors();
        }); // End removedNodes
      }); // End mutations
    }); // End MutationObserver

    $('div.inline-group').each(function (index, node) {
        observer.observe(node, { childList: true, subtree: true })
    });
  }); // End document.ready
})(django.jQuery);
{% endif %}
