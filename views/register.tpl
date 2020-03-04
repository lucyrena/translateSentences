<!-- register.tpl -->
<!DOCTYPE html>
<!-- <html lang="zh_cn"> -->
<html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0"/>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Sentence Practice</title>

  </head>
  <body align=center style="background-color: #E4E4E4;">
    <br><br><br>
  <form method="get" action="/registered">
		<input style="border-radius: 10px" type="text" class="username" name="username" placeholder="请输入用户名"><br><br>
		
		<input style="border-radius: 10px" type="password" class="password" name="password" placeholder="请输入注册密码"><br><br>
		<input style="border-radius: 10px" type="password" class="re_password" name="repassword" placeholder="再次输入密码"><br>
                 <span style="color: darkgoldenrod; margin-right: 5px"><br><br>
                 <a href="/login"><input type='button' value='已注册点这里' style="border-radius: 10px"></a></span><br>
                 
                 
		<div class="signin">
        <br>
                 <input style="border-radius: 10px" type="submit" class="submit" value="点击注册" >
        </div>
        
  </form>
  </body>
</html>
