<!-- viewresult.tpl -->
<!DOCTYPE html>
<html lang="zh_cn">
<html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0"/>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Sentence Practice</title>
    <style>
      table.diff {font-family:Courier; border:medium;table-layout:fixed;}
      .diff_header {background-color:#e0e0e0;table-layout:fixed;}
      td.diff_header {text-align:right;word-wrap: break-word;}
      .diff_next {background-color:#c0c0c0;word-wrap: break-word}
      .diff_add {background-color:#aaffaa;word-wrap: break-word}
      .diff_chg {background-color:#ffff77;word-wrap: break-word}
      .diff_sub {background-color:#ffaaaa;word-wrap: break-word}
      .gray {
            color: #e9e9e9;
            border: solid 1px #555;
            background: #6e6e6e;
            background: -webkit-gradient(linear, left top, left bottom, from(#888), to(#575757));
            background: -moz-linear-gradient(top,  #888,  #575757);
            filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#888888', endColorstr='#575757');
            }
    </style>

  </head>
  
  <body style="background-color: #E4E4E4;">
  
      <!-- <div style="padding:20px 200px;border:2px solid #000;margin:10px 100px 0px 100px">答案：<br></div> -->
      <!-- <div style="padding:20px 200px;border:2px solid #000;margin:10px 100px 0px 100px">已提交内容：<br></div> -->
      <div style="padding:20px 5%;border:2px solid #000;">待修改部分：<br>{{number}} {{!changed}}</div>
      <div style="padding:20px 5%;border:2px solid #000;">答案：<br>{{number}} {{answer}}</div>
      
      <p align=center>以上为参考答案和提交的句子的逐词对比（注意：若差异过大，则会被系统认为是完全不相同的句子，分别显示为红绿2种颜色）</p>
      
      <br>
      <div align=center >
          <a href="/sentence/{{number}}" name="top" id="top" class="gray">再练一遍</a>
          <a href="/goto/{{number}}" name="top" id="top" class="gray">下一题</a>
      </div>
  </body>
</html>