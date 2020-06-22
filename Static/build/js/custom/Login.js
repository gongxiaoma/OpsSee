$(document).ready(function () {

  $('#loginForm').validate({
    rules: {
      username: {
        required: true,
      },
      password: {
        required: true,
      }
    },
    messages: {
      username: {
        required: "请输入用户名",
      },
      password: {
        required: "请输入密码",
      }
     },
    errorElement: 'span',
    errorPlacement: function (error, element) {
      error.addClass('invalid-feedback');
      element.closest('.input-group').append(error);
    },
    highlight: function (element, errorClass, validClass) {
      $(element).addClass('is-invalid');
    },
    unhighlight: function (element, errorClass, validClass) {
      $(element).removeClass('is-invalid');
    }
  });
});