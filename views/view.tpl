<!-- view.tpl -->
<!DOCTYPE html>
<!-- <html lang="zh_cn"> -->
<html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0"/>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Sentence Practice</title>
    <!-- <link rel="stylesheet" type="text/css" href="stylesheet.css" /> -->
    <style>
    
      h1, form { text-align: center; }
      textarea { width:300px;height: 100px; background-color: #E4E4E4}
      em.date { color: #999; }
      div.global {width: 100%%;
                height: 100px;}
      div.content_menu {
                width: 100%%;
                height: 80px;
                text-align: center;
                background: tan;
                border-radius: .8em;padding: 1em;
                box-shadow: 0 0 0 .6em #655;
                outline: .6em solid #655;
                margin : 0px 16px 0px 16px;}
      div.content_body {width:80%%;}
      div.floor {clear: both;
                height: 100px;
                text-align:center}
      table.diff {font-family:Courier; border:medium;}
      .diff_header {background-color:#e0e0e0}
      td.diff_header {text-align:right}
      .diff_next {background-color:#c0c0c0;word-wrap: break-word;    word-break: normal; }
      .diff_add {background-color:#aaffaa;word-wrap: break-word;    word-break: normal; }
      .diff_chg {background-color:#ffff77;word-wrap: break-word;    word-break: normal; }
      .diff_sub {background-color:#ffaaaa;word-wrap: break-word;    word-break: normal; }
      div.box4 {
          width:80%%;
          height: auto;
          padding: 50px 20%%;
          background: tan;
          border-radius: .8em;padding: 1em;
          box-shadow: 0 0 0 0.6em #655;
          outline: .6em solid #655;
          margin : 20px 16px 20px 16px;}
      .gray {color: #e9e9e9;
            border: solid 1px #555;
            background: #6e6e6e;
            background: -webkit-gradient(linear, left top, left bottom, from(#888), to(#575757));
            background: -moz-linear-gradient(top,  #888,  #575757);
            filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#888888', endColorstr='#575757');
            }
    </style>

  </head>
  <body style="background-color: #E4E4E4;">
      <div>
            <div class="global">
                <h1>句子翻译练习</h1>
                <p align=center>已经练习时间：{{time}}分钟</p>
                <br>
            </div>
            
            <div class="content_menu">
                <b>开头段</b>
                    <a href="/sentence/0">背景句</a>
                    <a href="/sentence/2">观点句</a><br>
                <b>中间段</b>
                    <a href="/sentence/5">原因句</a>
                    <a href="/sentence/9">解释句</a>
                    <a href="/sentence/16">举例句</a>
                    <a href="/sentence/20">结果句</a><br>
                <b>中间段</b>
                    <a href="/sentence/23">假设句</a>
                    <a href="/sentence/26">对比句</a>
                    <a href="/sentence/28">转折句</a>
                    <a href="/sentence/31">反驳句</a><br>
                <b>结尾段</b>
                    <a href="/sentence/34">总结句</a>
                    <a href="/sentence/38">建议句</a>
            </div>
            
            <div class="content_body">
                <div class="box4" >
                <br>
                <br>
                    <div align=center style="width:80%; margin-left: auto;margin-right: auto; word-wrap:break-word;word-break:break-all;">
                    {{number}}. {{question}}
                    </div>
                <br>
                <br>
                    <form method=get action="/viewresult/{{number}}">
                      <div><textarea id="content" name="content"></textarea></div>
                      <br>
                      <br>
                      <div><button id="go" type="submit">提交答案</button></div>
                    </form>
                    <br>
                    
                    <div style="width:80%;margin-left: auto;margin-right: auto;">
                          <p id="con" style="display:none;">{{answer}}</p>
                          <div align=center>
                               <input button" type="button" onclick="hidetext()" value="不显示答案" align:"center"/>
                               <input button" type="button" onclick="showtext()" value="点此查看答案" align:"center"/>
                          </div>
                    </div>
                       <script>
                           function hidetext(){
                           document.getElementById("con").style.display="none";
                           }
                           function showtext(){
                           document.getElementById("con").style.display="block";
                           }
                        </script>
                     
                        <br>
                        <br>
                     <div align=center >
                         <a href="/returnto/{{number}}">练习上一句</a>
                         <a href="/goto/{{number}}">练习下一句</a>
                     </div>

                    <br>
                    <br>     
            </div>
           </div>
           
           <div class="floor">made by Rena</div>
           
        </div>
  </body>
</html>
