$(document).ready(function () {

  $.validator.addMethod("isPhone", function(value, element) {
          var length = value.length;
          var mobile = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1})|(17[0-9]{1}))+\d{8})$/;
          return this.optional(element) || (length == 11 && mobile.test(value));
         }, "请填写正确的手机号码");

  $.validator.addMethod("checkQQ",function(value,element,params){
          var checkQQ = /^[1-9][0-9]{4,19}$/;
          return this.optional(element)||(checkQQ.test(value));
         },"请输入正确的QQ号码");

  // $.validator.setDefaults({
  //   submitHandler: function () {
  //     alert( "Form successful submitted!" );
  //   }
  // });
  $('#registerForm').validate({
    rules: {
      username: {
        required: true,
        minlength: 2
      },
      password: {
        required: true,
        minlength: 5
      },
      confirm_password: {
        required: true,
        minlength: 5,
        equalTo: "#id_password"
      },
      email: {
        required: true,
        email: true
      },
      realname: {
        required: true,
      },
      qq: {
        required: true,
        checkQQ:true
      },
      wechat: {
        required: true,
      },
      mobile: {
        required: true,
        isPhone:true
      }
    },
    messages: {
      username: {
        required: "请输入用户名",
        minlength: "用户名不能小于2个字符组成"
      },
      password: {
        required: "请输入密码",
        minlength: "密码长度不能小于5个字符组成"
      },
      confirm_password: {
        required: "请输入密码",
        minlength: "密码长度不能小于5个字符组成",
        equalTo: "两次密码输入不一致"
      },
      email: {
        required: "请输入邮箱",
        email: "请输入一个正确的邮箱"
      },
      realname: {
        required: "请输入真实姓名",
      },
      qq: {
        required: "请输入QQ号码",
      },
      wechat: {
        required: "请输入微信号码",
      },
      mobile: {
        required: "请输入手机号码",
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