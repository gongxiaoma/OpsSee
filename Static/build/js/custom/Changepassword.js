$(document).ready(function () {
// 在键盘按下并释放及提交后验证提交表单
  $("#changepasswordForm").validate({
    rules: {
      password: {
        required: true,
      },
      new_password: {
        required: true,
        minlength: 5
      },
      confirm_password: {
        required: true,
        minlength: 5,
        equalTo: "#id_new_password"
      }
    },
    messages: {
      password: {
        required: "请输入旧密码",
      },
      new_password: {
        required: "请输入新密码",
        minlength: "密码长度不能小于5个字符组成"
      },
      confirm_password: {
        required: "请再次输入新密码",
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