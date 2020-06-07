$().ready(function() {

    $.validator.addMethod("isVerificationcode", function(value, element) {
          var verificationcode = /^\d{4}$/;
          return this.optional(element)||(verificationcode.test(value));
          }, "请填写正确的验证码");

// 在键盘按下并释放及提交后验证提交表单
  $("#forgotpasswordForm").validate({
    rules: {
      username: {
        required: true,
        minlength: 2
      },
      verificationcode: {
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
        required: "请输入用户名",
        minlength: "用户名不能小于2个字符组成"
      },
      verificationcode: {
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
     }
    })
});