$(document).ready(function () {

    $.validator.addMethod("isVerificationcode", function(value, element) {
          var verificationcode = /^\d{4}$/;
          return this.optional(element)||(verificationcode.test(value));
          }, "请填写正确的验证码");

// 在键盘按下并释放及提交后验证提交表单
  $("#forgotpasswordForm").validate({
    rules: {
      username: {
        required: true
      },
      verificationcode: {
        required: true,
        isVerificationcode: true
      },
      password: {
        required: true,
        minlength: 5
      },
      confirm_password: {
        required: true,
        minlength: 5,
        equalTo: "#password"
      }
    },
    messages: {
      username: {
        required: "请输入用户名"
      },
      verificationcode: {
        required: "请输入验证码"
      },
      password: {
        required: "请输入密码",
        minlength: "密码长度不能小于5个字符组成"
      },
      confirm_password: {
        required: "请输入密码",
        minlength: "密码长度不能小于5个字符组成",
        equalTo: "两次密码输入不一致"
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