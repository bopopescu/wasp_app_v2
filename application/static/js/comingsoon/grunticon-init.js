(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
"use strict";

/* global grunticon, jQuery */
var grunticonBasePath = typeof window.baseURL !== 'undefined' ? window.baseURL : '/assets/global';

(function () {
  var svgLoadedCORSCallback = function svgLoadedCORSCallback(callback) {
    if (grunticon.method !== 'svg') {
      return;
    }

    grunticon.ready(function () {
      grunticon.ajaxGet(grunticon.href, function () {
        // If stylesheet has been downloaded and embeded into the document, execute the callback and return.
        if (grunticon.loaded) {
          if (typeof callback === 'function') {
            callback();
          }

          return;
        }

        var style = document.createElement('style');
        style.setAttribute('data-src', grunticon.href);
        style.innerHTML = this.responseText; // If there is a linked CSS with same href, remove it to avoid conflict.

        var ref = grunticon.getCSS(grunticon.href);

        if (ref) {
          ref.parentNode.insertBefore(style, ref);
          ref.parentNode.removeChild(ref);
          grunticon.embedIcons(grunticon.getIcons(style));

          if (typeof callback === 'function') {
            callback();
          }
        }

        grunticon.loaded = true; // Notify other component that grunticon is fully loaded.

        jQuery(document).trigger('grunticon-loaded');
      });
    });
  };

  grunticon([grunticonBasePath + '/icons/icons.data.svg.css', grunticonBasePath + '/icons/icons.data.png.css', grunticonBasePath + '/icons/icons.fallback.css'], svgLoadedCORSCallback);
})();

},{}]},{},[1])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm5vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCJzcmMvYXNzZXRzL2pzL2dydW50aWNvbi1pbml0LmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7QUNBQTtBQUNBLElBQUksaUJBQWlCLEdBQUcsT0FBTyxNQUFNLENBQUMsT0FBZCxLQUEwQixXQUExQixHQUF3QyxNQUFNLENBQUMsT0FBL0MsR0FBeUQsZ0JBQWpGOztBQUNBLENBQUMsWUFBVztBQUNWLE1BQUkscUJBQXFCLEdBQUcsU0FBeEIscUJBQXdCLENBQVMsUUFBVCxFQUFtQjtBQUM3QyxRQUFJLFNBQVMsQ0FBQyxNQUFWLEtBQXFCLEtBQXpCLEVBQWdDO0FBQzlCO0FBQ0Q7O0FBQ0QsSUFBQSxTQUFTLENBQUMsS0FBVixDQUFnQixZQUFXO0FBQ3pCLE1BQUEsU0FBUyxDQUFDLE9BQVYsQ0FBa0IsU0FBUyxDQUFDLElBQTVCLEVBQWtDLFlBQVc7QUFDM0M7QUFDQSxZQUFJLFNBQVMsQ0FBQyxNQUFkLEVBQXNCO0FBQ3BCLGNBQUksT0FBTyxRQUFQLEtBQW9CLFVBQXhCLEVBQW9DO0FBQ2xDLFlBQUEsUUFBUTtBQUNUOztBQUNEO0FBQ0Q7O0FBQ0QsWUFBSSxLQUFLLEdBQUcsUUFBUSxDQUFDLGFBQVQsQ0FBdUIsT0FBdkIsQ0FBWjtBQUNBLFFBQUEsS0FBSyxDQUFDLFlBQU4sQ0FBbUIsVUFBbkIsRUFBK0IsU0FBUyxDQUFDLElBQXpDO0FBQ0EsUUFBQSxLQUFLLENBQUMsU0FBTixHQUFrQixLQUFLLFlBQXZCLENBVjJDLENBVzNDOztBQUNBLFlBQUksR0FBRyxHQUFHLFNBQVMsQ0FBQyxNQUFWLENBQWlCLFNBQVMsQ0FBQyxJQUEzQixDQUFWOztBQUNBLFlBQUksR0FBSixFQUFTO0FBQ1AsVUFBQSxHQUFHLENBQUMsVUFBSixDQUFlLFlBQWYsQ0FBNEIsS0FBNUIsRUFBbUMsR0FBbkM7QUFDQSxVQUFBLEdBQUcsQ0FBQyxVQUFKLENBQWUsV0FBZixDQUEyQixHQUEzQjtBQUNBLFVBQUEsU0FBUyxDQUFDLFVBQVYsQ0FBcUIsU0FBUyxDQUFDLFFBQVYsQ0FBbUIsS0FBbkIsQ0FBckI7O0FBQ0EsY0FBSSxPQUFPLFFBQVAsS0FBb0IsVUFBeEIsRUFBb0M7QUFDbEMsWUFBQSxRQUFRO0FBQ1Q7QUFDRjs7QUFDRCxRQUFBLFNBQVMsQ0FBQyxNQUFWLEdBQW1CLElBQW5CLENBckIyQyxDQXNCM0M7O0FBQ0EsUUFBQSxNQUFNLENBQUMsUUFBRCxDQUFOLENBQWlCLE9BQWpCLENBQXlCLGtCQUF6QjtBQUNELE9BeEJEO0FBeUJELEtBMUJEO0FBMkJELEdBL0JEOztBQWlDQSxFQUFBLFNBQVMsQ0FDUCxDQUNFLGlCQUFpQixHQUFHLDJCQUR0QixFQUVFLGlCQUFpQixHQUFHLDJCQUZ0QixFQUdFLGlCQUFpQixHQUFHLDJCQUh0QixDQURPLEVBTVAscUJBTk8sQ0FBVDtBQVFELENBMUNEIiwiZmlsZSI6ImdlbmVyYXRlZC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzQ29udGVudCI6WyIoZnVuY3Rpb24oKXtmdW5jdGlvbiByKGUsbix0KXtmdW5jdGlvbiBvKGksZil7aWYoIW5baV0pe2lmKCFlW2ldKXt2YXIgYz1cImZ1bmN0aW9uXCI9PXR5cGVvZiByZXF1aXJlJiZyZXF1aXJlO2lmKCFmJiZjKXJldHVybiBjKGksITApO2lmKHUpcmV0dXJuIHUoaSwhMCk7dmFyIGE9bmV3IEVycm9yKFwiQ2Fubm90IGZpbmQgbW9kdWxlICdcIitpK1wiJ1wiKTt0aHJvdyBhLmNvZGU9XCJNT0RVTEVfTk9UX0ZPVU5EXCIsYX12YXIgcD1uW2ldPXtleHBvcnRzOnt9fTtlW2ldWzBdLmNhbGwocC5leHBvcnRzLGZ1bmN0aW9uKHIpe3ZhciBuPWVbaV1bMV1bcl07cmV0dXJuIG8obnx8cil9LHAscC5leHBvcnRzLHIsZSxuLHQpfXJldHVybiBuW2ldLmV4cG9ydHN9Zm9yKHZhciB1PVwiZnVuY3Rpb25cIj09dHlwZW9mIHJlcXVpcmUmJnJlcXVpcmUsaT0wO2k8dC5sZW5ndGg7aSsrKW8odFtpXSk7cmV0dXJuIG99cmV0dXJuIHJ9KSgpIiwiLyogZ2xvYmFsIGdydW50aWNvbiwgalF1ZXJ5ICovXG52YXIgZ3J1bnRpY29uQmFzZVBhdGggPSB0eXBlb2Ygd2luZG93LmJhc2VVUkwgIT09ICd1bmRlZmluZWQnID8gd2luZG93LmJhc2VVUkwgOiAnL2Fzc2V0cy9nbG9iYWwnO1xuKGZ1bmN0aW9uKCkge1xuICB2YXIgc3ZnTG9hZGVkQ09SU0NhbGxiYWNrID0gZnVuY3Rpb24oY2FsbGJhY2spIHtcbiAgICBpZiAoZ3J1bnRpY29uLm1ldGhvZCAhPT0gJ3N2ZycpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgZ3J1bnRpY29uLnJlYWR5KGZ1bmN0aW9uKCkge1xuICAgICAgZ3J1bnRpY29uLmFqYXhHZXQoZ3J1bnRpY29uLmhyZWYsIGZ1bmN0aW9uKCkge1xuICAgICAgICAvLyBJZiBzdHlsZXNoZWV0IGhhcyBiZWVuIGRvd25sb2FkZWQgYW5kIGVtYmVkZWQgaW50byB0aGUgZG9jdW1lbnQsIGV4ZWN1dGUgdGhlIGNhbGxiYWNrIGFuZCByZXR1cm4uXG4gICAgICAgIGlmIChncnVudGljb24ubG9hZGVkKSB7XG4gICAgICAgICAgaWYgKHR5cGVvZiBjYWxsYmFjayA9PT0gJ2Z1bmN0aW9uJykge1xuICAgICAgICAgICAgY2FsbGJhY2soKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIHZhciBzdHlsZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3N0eWxlJyk7XG4gICAgICAgIHN0eWxlLnNldEF0dHJpYnV0ZSgnZGF0YS1zcmMnLCBncnVudGljb24uaHJlZik7XG4gICAgICAgIHN0eWxlLmlubmVySFRNTCA9IHRoaXMucmVzcG9uc2VUZXh0O1xuICAgICAgICAvLyBJZiB0aGVyZSBpcyBhIGxpbmtlZCBDU1Mgd2l0aCBzYW1lIGhyZWYsIHJlbW92ZSBpdCB0byBhdm9pZCBjb25mbGljdC5cbiAgICAgICAgdmFyIHJlZiA9IGdydW50aWNvbi5nZXRDU1MoZ3J1bnRpY29uLmhyZWYpO1xuICAgICAgICBpZiAocmVmKSB7XG4gICAgICAgICAgcmVmLnBhcmVudE5vZGUuaW5zZXJ0QmVmb3JlKHN0eWxlLCByZWYpO1xuICAgICAgICAgIHJlZi5wYXJlbnROb2RlLnJlbW92ZUNoaWxkKHJlZik7XG4gICAgICAgICAgZ3J1bnRpY29uLmVtYmVkSWNvbnMoZ3J1bnRpY29uLmdldEljb25zKHN0eWxlKSk7XG4gICAgICAgICAgaWYgKHR5cGVvZiBjYWxsYmFjayA9PT0gJ2Z1bmN0aW9uJykge1xuICAgICAgICAgICAgY2FsbGJhY2soKTtcbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgICAgZ3J1bnRpY29uLmxvYWRlZCA9IHRydWU7XG4gICAgICAgIC8vIE5vdGlmeSBvdGhlciBjb21wb25lbnQgdGhhdCBncnVudGljb24gaXMgZnVsbHkgbG9hZGVkLlxuICAgICAgICBqUXVlcnkoZG9jdW1lbnQpLnRyaWdnZXIoJ2dydW50aWNvbi1sb2FkZWQnKTtcbiAgICAgIH0pO1xuICAgIH0pO1xuICB9O1xuXG4gIGdydW50aWNvbihcbiAgICBbXG4gICAgICBncnVudGljb25CYXNlUGF0aCArICcvaWNvbnMvaWNvbnMuZGF0YS5zdmcuY3NzJyxcbiAgICAgIGdydW50aWNvbkJhc2VQYXRoICsgJy9pY29ucy9pY29ucy5kYXRhLnBuZy5jc3MnLFxuICAgICAgZ3J1bnRpY29uQmFzZVBhdGggKyAnL2ljb25zL2ljb25zLmZhbGxiYWNrLmNzcydcbiAgICBdLFxuICAgIHN2Z0xvYWRlZENPUlNDYWxsYmFja1xuICApO1xufSkoKTtcbiJdfQ==
