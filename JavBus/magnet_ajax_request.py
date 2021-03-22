import requests
import re
import random

headers = {
    'Host': 'www.javbus.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Refer': 'https://www.javbus.com/SSIS-013',
}

gid = '45864938377'
lang = 'zh'
img = 'https://pics.javbus.com/cover/853n_b.jpg'
uc = '0'

url = f"https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid={gid}&lang={lang}&img={img}&uc={uc}&floor={int(random.random() * 1000) + 1}"

proxy = {
    'http': 'http://192.168.1.8:7890',
    'https': 'https://192.168.1.8:7890',
}

# response = requests.get(url, proxies=proxy, verify=False)
# if response.status_code == 200:
#     print(response.text)
text_tmp = """
  <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="renderer" content="webkit">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - JavBus</title>
<meta name="keywords" content="JUL-515,Madonna,已婚婦女,數位馬賽克,成熟的女人,單體作品,戲劇,通姦,母乳,DMM獨家,高畫質">
<meta name="description" content="【發行日期】2021-03-21，【長度】120分鐘，(JUL-515)子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ">
<link rel="alternate" href="https://www.javbus.com/en/JUL-515" hreflang="en" />
<link rel="alternate" href="https://www.javbus.com/ja/JUL-515" hreflang="ja" />
<link rel="alternate" href="https://www.javbus.com/ko/JUL-515" hreflang="ko" />
<link rel="alternate" href="https://www.javbus.com/JUL-515" hreflang="zh" />
<link rel="alternate" href="https://www.javbus.com/JUL-515" hreflang="x-default" />
<link rel="canonical" href="https://www.javbus.com/JUL-515" />
<link href='https://www.javbus.com/css/bootstrap.min.css' rel='stylesheet'>
<link href='https://www.javbus.com/css/bootstrap-theme.min.css' rel='stylesheet'>
<link href='https://www.javbus.com/css/magnific-popup.css' rel='stylesheet'>
<link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/base.css?v=4.4'>
<link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/nav.overlay.css?v=3.9.8' >
<script src='https://www.javbus.com/js/jquery.min.js'></script>
<script src='https://www.javbus.com/js/bootstrap.min.js'></script>
<script src='https://www.javbus.com/js/jquery.magnific-popup.min.js'></script>
<script src='https://www.javbus.com/js/jquery.cookie.min.js'></script>
<script src='https://www.javbus.com/js/base.js'></script>
<script src='https://www.javbus.com/js/bootstrap-hover-dropdown.js'></script>
<!--[if lt IE 9]> <script src='https://www.javbus.com/js/html5shiv.min.js'></script><script src='https://www.javbus.com/js/respond.min.js'></script><![endif]-->
</head>
<body>
<script language="JavaScript">
var mod = 0;
var lang = 'zh';
var info = '搜尋 識別碼, 影片, 演員';
function searchs(obj){
	var searchinput = $("#"+obj);
	if(searchinput.val()=='')
	{
		$('#magnet-url-post').trigger("click");
		   return false;
	}
	else
	{
		//$('#search-loading').show();
		window.open("https://www.javbus.com/search/"+encodeURIComponent($.trim(searchinput.val()))+"&type=&parent=ce");
	}
}

$(function(){
	
	var url ='https://www.javbus.com/ajax/search-modal.php?floor='+Math.floor(Math.random()*1000+1)+'&lang='+lang;
       $.ajax({url: url,type: 'GET',success: function(msg){
			$("#searchModal").append(msg);
	   }});
});
</script>
<div id="search-loading">
    <table class="search-loading-box" border="0" cellpadding="0" cellspacing="0">
        <tbody>
            <tr>
                <td align="center">
                    <table height="80" width="100%" border="0" cellpadding="0" cellspacing="0">
                        <tbody>
                            <tr>
                                <td height="40" align="center">
                                	<div class="search-loading-text">搜尋中...</div>
                                </td>
                            </tr>
                            <tr>
                                <td height="40" align="center">
                                    <img src="https://www.javbus.com/images/search_loading.gif" border="0">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Modal Search -->
<div id="searchModal" class="modal fade" tabindex="-1" role="dialog"></div>

<nav class="navbar navbar-default navbar-fixed-top top-bar" style="z-index:900">
    <div class="container-fluid">
        <div class="navbar-header mh50">
            <a href="https://www.javbus.com/">
                <img class="hidden-xs" height="50" alt="JavBus" src="https://www.javbus.com/images/logo.png" style="height:40px; margin-top:5px;">
                <img class="visible-xs-inline" height="50" alt="JavBus" src="https://www.javbus.com/images/logo.png">
            </a>

            

            <div class="btn-group pull-right visible-xs-inline" role="group" style="margin:8px 8px 0 0;">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <span class="glyphicon glyphicon-globe"></span>  <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" role="menu">
                    <li><a href="https://www.javbus.com/en/JUL-515">English</a></li>
                    <li><a href="https://www.javbus.com/ja/JUL-515">日本语</a></li>
                    <li><a href="https://www.javbus.com/ko/JUL-515">한국의</a></li>
                    <li><a href="https://www.javbus.com/JUL-515">中文</a></li>
                </ul>
            </div>
 
 		 
		          
 
        </div>
 
        <div id="navbar" class="collapse navbar-collapse">
            <div class="navbar-form navbar-left fullsearch-form">
                <div class="input-group">
                    <input id="search-input" type="text" class="form-control" placeholder="搜尋 識別碼, 影片, 演員">
                    <span class="input-group-btn">
                    <button class="btn btn-default" type="submit" onClick="searchs('search-input')">搜尋</button>
                    </span>
                </div>
            </div>
            <ul class="nav navbar-nav">
            	<li class="active"><a href="https://www.javbus.com/">有碼</a></li>
                <li><a href="https://www.javbus.com/uncensored">無碼</a></li>
                <li class="hidden-md hidden-sm"><!-- <div class="icon-new"></div> --><a href="https://www.javbus.org/">歐美</a></li>
				            
                <li class="dropdown hidden-sm ">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false">類別 <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="https://www.javbus.com/genre">有碼類別</a></li>
                        <li><a href="https://www.javbus.com/uncensored/genre">無碼類別</a></li>
                    </ul>
                </li>
                <li class="dropdown hidden-sm ">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false">女優 <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="https://www.javbus.com/actresses">有碼女優</a></li>
                        <li><a href="https://www.javbus.com/uncensored/actresses">無碼女優</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="https://www.javbus.com/" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-menu-hamburger"></span></a>
                    <ul class="dropdown-menu" role="menu">
                    	<li class="visible-md-block visible-sm-block"><a href="https://www.javbus.org/">歐美</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/genre">有碼類別</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/uncensored/genre">無碼類別</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/actresses">有碼女優</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/uncensored/actresses">無碼女優</a></li>
                        <li><a href="https://www.javbus.com/genre/hd">高清</a></li>
                        <li><a href="https://www.javbus.com/genre/sub">字幕</a></li>
                    </ul>
				</li>
            </ul>
            
            
            
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-globe" style="font-size:12px;"></span> <span class="hidden-md hidden-sm">English</span> <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="https://www.javbus.com/en/JUL-515">English</a></li>
                        <li><a href="https://www.javbus.com/ja/JUL-515">日本语</a></li>
                        <li><a href="https://www.javbus.com/ko/JUL-515">한국의</a></li>
                        <li><a href="https://www.javbus.com/JUL-515">中文</a></li>
                    </ul>
                </li>
            </ul>

            
        	   
        </div>
        <!--/.nav-collapse -->
    </div>
</nav>
<div class="row visible-xs-inline footer-bar">
    <div class="col-xs-3 text-center">
        <a id="menu" class="btn btn-default trigger-overlay"><span class="glyphicon glyphicon-align-justify"></span></a>
    </div>
    <div class="col-xs-3 text-center">
         </div>
    <div class="col-xs-3 text-center">
        </div>
    <div class="col-xs-3 text-center">
        <a id="back" class="btn btn-default" href="javascript:window.history.back()"><span class="glyphicon glyphicon-share-alt flipx"></span></a>
    </div>
</div>
<script src='https://www.javbus.com/js/focus.js?v=8.7'></script>  <link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/movie.css?v=2.8' >
<link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/movie-box.css' >
<script>
	var gid = 45917399600;
	var uc = 0;
	var img = 'https://pics.javbus.com/cover/85g4_b.jpg';
</script>


<div class="ad-list">
<div class="hidden-xs text-center"><script data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="706613" data-width="728" data-height="90"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":706613});</script></div></div><input id="token" type="hidden" name="token" value="80faV4P8xcAoLXAcH1vViJq8gk6011B6wQQ1XPJW7XPzPfv5+Qf0shLE2KF2701Q3S0jC+SB1mFsACnC4ZTqtCrk4WsvEV4MrTL7">
<div class="container">
    <h3>JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ</h3>
    <div class="row movie">
        <div class="col-md-9 screencap">
            <a class="bigImage" href="https://pics.javbus.com/cover/85g4_b.jpg"><img src="https://pics.javbus.com/cover/85g4_b.jpg" title="子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ"></a>
        </div>
        <div class="col-md-3 info">
            <p><span class="header">識別碼:</span> <span style="color:#CC0000;">JUL-515</span>
            </p>
            <p><span class="header">發行日期:</span> 2021-03-21</p>
            <p><span class="header">長度:</span> 120分鐘</p>
                        <p><span class="header">導演:</span> <a href="https://www.javbus.com/director/3wd">木村浩之</a></p>
                                    <p><span class="header">製作商:</span> <a href="https://www.javbus.com/studio/6n">マドンナ</a>
            </p>                        <p><span class="header">發行商:</span> <a href="https://www.javbus.com/label/7l">Madonna</a>
            </p>                        <p class="header">類別:<span id="genre-toggle" class="glyphicon glyphicon-plus" style="cursor: pointer;"></span></p>
            <p>            <span class="genre"><label><input type="checkbox" name="gr_sel" value="29"><a href="https://www.javbus.com/genre/29">已婚婦女</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="31"><a href="https://www.javbus.com/genre/31">數位馬賽克</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="13"><a href="https://www.javbus.com/genre/13">成熟的女人</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="f"><a href="https://www.javbus.com/genre/f">單體作品</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="4u"><a href="https://www.javbus.com/genre/4u">戲劇</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="3g"><a href="https://www.javbus.com/genre/3g">通姦</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="47"><a href="https://www.javbus.com/genre/47">母乳</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="g"><a href="https://www.javbus.com/genre/g">DMM獨家</a></label></span>
                        <span class="genre"><label><input type="checkbox" name="gr_sel" value="4o"><a href="https://www.javbus.com/genre/4o">高畫質</a></label></span>
            <span class="genre"><button id="gr_btn" type="button" class="btn">多選提交</button></span>
            </p>            <p class="star-show"><span class="header" style="cursor: pointer;">演員</span>:<span id="star-toggle" class="glyphicon glyphicon-plus" style="cursor: pointer;"></span></p>
                
                <ul>
                                      <div id="star_q87" class="star-box star-box-common star-box-up idol-box">
                      <li>
                          <a href="https://www.javbus.com/star/q87"><img src="https://pics.javbus.com/actress/q87_a.jpg" title="成澤ひなみ"></a>
                          <div class="star-name"><a href="https://www.javbus.com/star/q87" title="成澤ひなみ">成澤ひなみ</a></div>
                      </li>
                    </div>
                                  </ul>
                
			<p>
						<span class="genre" onmouseover="hoverdiv(event,'star_q87')" onmouseout="hoverdiv(event,'star_q87')">
					<a href="https://www.javbus.com/star/q87">成澤ひなみ</a>
				</span>
                					</p>
                     
			                  
        </div>
    </div>

<div id="star-div">
	<h4 id="star-hide" style="cursor: pointer;">演員 <span class="glyphicon glyphicon-minus"></span></h4>
    <div id="avatar-waterfall">
            <a class="avatar-box" href="https://www.javbus.com/star/q87">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/actress/q87_a.jpg" title="成澤ひなみ">
            </div>
            <span>成澤ひなみ</span>
        </a>
        
    </div>
  
</div>

<h4 id="mag-submit-show" style="cursor: pointer;">磁力連結投稿 <span id="mag-submit-toggle" class="glyphicon glyphicon-plus"></span></h4>
	<div id="mag-submit" class="movie" style="padding:30px 20px 30px 5px;">
		<div id="mag-submit-hide" class="close" style="margin:-25px -13px 0 0;">&times;</div>
          <div class="col-md-11 col-xs-10">
            <div class="input-group">
              <div class="input-group-addon">magnet地址:</div>
              <input type="text" class="form-control" id="appendedInputButton">
            </div>
          </div>
          <button type="button" class="btn btn-default col-md-1 col-xs-2" onClick="checktxt()" data-toggle="modal" data-target="#magneturlpost">分享</button>
    </div>
<!-- Magnet Verify Modal -->
<div id="magneturlpost" class="modal fade" tabindex="-1" role="dialog"></div>
		<div class="movie" style="padding:12px; margin-top:15px">
        <table id="magnet-table" class="table table-condensed table-striped table-hover" style="margin-bottom:0;">
            <tr style="font-weight:bold;">
              <td>磁力名稱 <span class="glyphicon glyphicon-magnet"></span></td>
              <td style="text-align:center;white-space:nowrap">檔案大小</td>
              <td style="text-align:center;white-space:nowrap">分享日期</td>
            </tr>
        </table>
            <div id="movie-loading">
                <table width="120" border="0" cellpadding="5" cellspacing="0">
                    <tbody>
                        <tr>
                            <td align="center">
                                <font class="ajax-text"><img src="https://www.javbus.com/images/movie_loading.gif" border="0"></font>
                            </td>
                            <td align="center">
                                <font class="ajax-text">讀取中...</font>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
		</div>
 


 
    
    <h4>樣品圖像</h4>
    <div id="sample-waterfall">
	<a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-1.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_1.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 1"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-2.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_2.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 2"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-3.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_3.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 3"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-4.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_4.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 4"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-5.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_5.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 5"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-6.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_6.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 6"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-7.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_7.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 7"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-8.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_8.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 8"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-9.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_9.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 9"></div></a>        <a class="sample-box" href="https://pics.dmm.co.jp/digital/video/jul00515/jul00515jp-10.jpg"><div class="photo-frame"><img src="https://pics.javbus.com/sample/85g4_10.jpg" title="JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ - 樣品圖像 - 10"></div></a>            </div>
 
<div class="clearfix"></div>
<h4 style="position:relative">推薦 <a href="javascript:bootstr(1);"><span id="urad2" class="label label-default"><span class="left-urad2">投放廣告</span><span class="glyphicon glyphicon-envelope"></span></span></a></h4>
<div class="row">
<div class="col-xs-12 col-md-4 text-center ptb10"><a href="https://l.tyrantdb.com/cC1uatoU" target="_blank" rel="nofollow"><img src="/ads/r18_db_300x250.gif" width="300" height="250"></a></div><div class="col-xs-12 col-md-4 text-center ptb10"><script type="text/javascript" data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="464076" data-width="300" data-height="250"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":464076});</script></div><div class="col-xs-12 col-md-4 text-center ptb10"><script type="text/javascript" data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="796384" data-width="300" data-height="250"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":796384});</script></div>
</div>
	<h4>同類影片</h4>
    <div id="related-waterfall" class="mb20">
            <a title="才色兼備の王道美熟女マドンナ専属第3弾！！ 母の友人 北川真由香" class="movie-box" href="https://www.javbus.com/JUL-459" style="display:inline-block; margin:5px;">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/thumb/82xw.jpg">
            </div>
            <div class="photo-info" style="height:36px; overflow:hidden; text-align:center;">
                <span>才色兼備の王道美熟女マドンナ専属第3弾！！ 母の友人 北川真由香</span>
            </div>
        </a>
            <a title="送迎手の僕は社長夫人と不貞ドライブへ―。 北条麻妃" class="movie-box" href="https://www.javbus.com/JUL-465" style="display:inline-block; margin:5px;">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/thumb/82xq.jpg">
            </div>
            <div class="photo-info" style="height:36px; overflow:hidden; text-align:center;">
                <span>送迎手の僕は社長夫人と不貞ドライブへ―。 北条麻妃</span>
            </div>
        </a>
            <a title="マドンナ専属・白石茉莉奈×熟れコミ 原作:ビフィダス「不倫托卵温泉」-榊妙子さんの非日常 初めての不倫に溺れるウブな人妻の痴態を忠実に実写化！！" class="movie-box" href="https://www.javbus.com/URE-062" style="display:inline-block; margin:5px;">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/thumb/826a.jpg">
            </div>
            <div class="photo-info" style="height:36px; overflow:hidden; text-align:center;">
                <span>マドンナ専属・白石茉莉奈×熟れコミ 原作:ビフィダス「不倫托卵温泉」-榊妙子さんの非日常 初めての不倫に溺れるウブな人妻の痴態を忠実に実写化！！</span>
            </div>
        </a>
            <a title="Madonna専属 白雪妻 第2弾！！ 汗、唾液、愛液、すべての体液が絡み合う…真夏の濃密不倫セックス。 広瀬梓" class="movie-box" href="https://www.javbus.com/JUL-423" style="display:inline-block; margin:5px;">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/thumb/80zw.jpg">
            </div>
            <div class="photo-info" style="height:36px; overflow:hidden; text-align:center;">
                <span>Madonna専属 白雪妻 第2弾！！ 汗、唾液、愛液、すべての体液が絡み合う…真夏の濃密不倫セックス。 広瀬梓</span>
            </div>
        </a>
            <a title="地元へ帰省した三日間、人妻になっていた憧れの叔母さんと時を忘れて愛し合った記録―。 加藤ツバキ" class="movie-box" href="https://www.javbus.com/JUL-435" style="display:inline-block; margin:5px;">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/thumb/80zk.jpg">
            </div>
            <div class="photo-info" style="height:36px; overflow:hidden; text-align:center;">
                <span>地元へ帰省した三日間、人妻になっていた憧れの叔母さんと時を忘れて愛し合った記録―。 加藤ツバキ</span>
            </div>
        </a>
            <a title="綺麗なお姉さん系《母乳ママ》マドンナ専属 第2弾！！ 美しい妻の妹 背徳のミルクシャワー さとう白音" class="movie-box" href="https://www.javbus.com/JUL-206" style="display:inline-block; margin:5px;">
            <div class="photo-frame">
                <img src="https://pics.javbus.com/thumb/7ng7.jpg">
            </div>
            <div class="photo-info" style="height:36px; overflow:hidden; text-align:center;">
                <span>綺麗なお姉さん系《母乳ママ》マドンナ専属 第2弾！！ 美しい妻の妹 背徳のミルクシャワー さとう白音</span>
            </div>
        </a>
        </div>



<script language="JavaScript">
(function($){
	$('img.img').each(function(){
    var image=new Image();
    image.src=this.src;
    if(image.complete){
        cutImgz(this);
    } else{
        this.onload=function(){
            cutImgz(this);
        }
    }
	});
})(jQuery);

function cutImgz(obj){
    var image=new Image();
    image.src=obj.src;
    $this=$(obj);
	var w = image.width;
	var h = image.height;
	var p = w/h;
    if(p>1.38&&p<1.40){
        $this.addClass("m1000giri");
    }
    if(p>0.99&&p<1.01){
        $this.addClass("mpacopacomama");
    }
    if(p>1.11&&p<1.13){
        $this.addClass("mcaribbeancom");
    }
    if(p>1.77&&p<1.78){
        $this.addClass("mcaribbeancom2");
    }
    if(p>0.59&&p<0.61){
        $this.addClass("m1pondo");
    }
    if(p>0.65&&p<0.67){
        $this.addClass("mtokyohot");
    }
    if(p>1.78&&p<1.79){
        $this.addClass("mheyzo");
    }
}
</script>
    
    
    <script>
        (function($){
        $('.bigImage').magnificPopup({
            type: 'image',
            closeOnContentClick: true,
            closeBtnInside: false,
            fixedContentPos: true,
            mainClass: 'mfp-no-margins mfp-with-zoom',
            image: {
                verticalFit: true,
                titleSrc: function(item) {
                    return "JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ";
                }
            },
            zoom: {
                enabled: true,
                duration: 300
            }
        });
        
        $('#sample-waterfall').magnificPopup({
            delegate: 'a',
            type: 'image',
            closeOnContentClick: false,
            closeBtnInside: false,
            mainClass: 'mfp-with-zoom mfp-img-mobile',
            image: {
                verticalFit: true,
                titleSrc: function(item) {
                    return "JUL-515 子育てに追われる新米イクメンの僕は授乳室で母乳ママに誘惑されて―。 成澤ひなみ";
                }
            },
            gallery: {
                enabled: true
            },
            zoom: {
                enabled: true,
                duration: 300,
                opener: function(element) {
                    return element.find('img');
                }
            }
            
        });
        })(jQuery);
		
		$("#gr_btn").click(function() {
			var t = "";
			$("input[name='gr_sel']:checkbox").each(function() {
				$(this).is(":checked") && (t += $(this).val() + "-")
			}), "" != t && (t = t.substring(0, t.length - 1), window.location.href = "genre/" + t)
		});
</script>
</div>


<div class="ad-list">
<div class="hidden-xs text-center"><script data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="365002" data-width="728" data-height="90"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":365002});</script></div></div>
<script src='https://www.javbus.com/js/gallery.js?v=2.9'></script>
<footer class="footer hidden-xs">
	<div class="container-fluid">
        <p><a href="https://www.javbus.com/doc/terms">Terms</a> / <a href="https://www.javbus.com/doc/privacy">Privacy</a> / <a href="https://www.javbus.com/doc/usc">2257</a> / <a href="http://www.rtalabel.org/" target="_blank" rel="external nofollow">RTA</a> / <a href="javascript:bootstr(1);" r>廣告投放</a> / <a href="javascript:bootstr(2);" >聯絡我們</a><br /><a href="#formModal" id="adscontact" data-toggle="modal"></a>
        Copyright © 2013 JavBus. All Rights Reserved. All other trademarks and copyrights are the property of their respective holders. The reviews and comments expressed at or through this website are the opinions of the individual author and do not reflect the opinions or views of JavBus. JavBus is not responsible for the accuracy of any of the information supplied here.</p>
	</div>
</footer>
<div class="visible-xs-block footer-bar-placeholder"></div>

<script language=javascript>
    function bootstr(type){
    	ads = "廣告投放";
    	contact = "聯絡我們";
    	translate = "翻譯";
    	$("#adstype").val(type);
    	if(type==1){
    		$("#contactModalLab").html(ads);
    		$("#qqskype").show();
    		$("#transinfo").hide();
    		$("#translanguage").hide();
    		$("#mailcontent").show();
    	}else if(type==2){
    		$("#contactModalLab").html(contact);
    		$("#qqskype").show();
    		$("#transinfo").hide();
    		$("#translanguage").hide();
    		$("#mailcontent").show();
    	}else if(type==3){
    		$("#contactModalLab").html(translate);
    		$("#qqskype").hide();
    		$("#transinfo").show();
    		$("#translanguage").show();
    		$("#mailcontent").hide();
    	}
    	$("#adscontact").trigger("click");
		getverifycode();
    };
    function getverifycode(){
       $('#verify').attr("src","/post/verify?"+Math.random()*10000);
    };
    function IsMail(mail){
     var remail= /^([a-zA-Z0-9_-])+(\.)?([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
     return(remail.test(mail));
    };
    function checkform(){
    	var post = true;
      if($("#verifycode").val().length!=5){
    	  	alert("驗證碼輸入錯誤!")
    		$("#verifycode").focus();
    		post = false;
    	  }
      if($("#contact").val().length>255){
    	  	alert("聯繫方式字數過多!")
    		$("#contact").focus();
    		post = false;
    	  }
      
      if(!IsMail($("#mail").val())){
    	alert("請輸入正確的電郵地址!")
     	$("#mail").focus();
        post = false;
      }
      
      if($("#intention").val().length>25500){
    	  	alert("投放意向字數過多!")
    		$("#intention").focus();
    		post = false;
    	  }
    	  
      if($("#trans").val().length>255){
    	  	alert("Too many words in your language textbox!")
    		$("#intention").focus();
    		post = false;
    	  }
      if(post== true){
    	  $("#modalclose").trigger("click");
    	  $("#postform").attr("action", "/post/contact");
    	  $("#postform").submit();
    	}
      return post;
    };
</script>

<script>
$("#showmag,#cellshowmag,#resultshowmag").click(function(){
	$.cookie("existmag", "mag",{expires:365,path:'/'});
	location.reload()
});

$("#showall,#cellshowall,#resultshowall").click(function(){
	$.cookie("existmag", "all",{expires:365,path:'/'});
	location.reload()
});
$("#showonline").click(function(){
	$.cookie("existmag", "online",{expires:365,path:'/'});
	location.reload()
});
$(".info .mypointer").click(function(){
	var obj = $(this);
	var code = obj.attr('value');
	var token = $("#token").val();
	var e = "../ajax/addfavorite.php?code=" + encodeURIComponent(code) + "&token=" + encodeURIComponent(token) + "&floor=" + Math.floor(Math.random() * 1e3 + 1);
    $.ajax({
        url: e,
        type: "POST",
		//dataType: "json",
		cache:false,
        success: function (json) {
			//obj.html(json);
			ajaxobj=eval("("+json+")");
			if(ajaxobj.act=='err'){
				alert('收藏次數達上限，請稍候再試');
			}else{
				obj.html(ajaxobj.act);
				obj.attr('value',ajaxobj.code);
				obj.attr('title',ajaxobj.title);
				$("#token").val(ajaxobj.token);
			}
        }
    });
});

$(".glyphicon-heart-empty").hover(function () {
    $(this).removeClass('glyphicon-heart-empty');
	$(this).addClass('glyphicon-heart');
}, function () {
    $(this).removeClass('glyphicon-heart');
    $(this).addClass('glyphicon-heart-empty');
});
$(".glyphicon-heart").hover(function () {
    $(this).removeClass('glyphicon-heart');
	$(this).addClass('glyphicon-heart-empty');
}, function () {
    $(this).removeClass('glyphicon-heart-empty');
    $(this).addClass('glyphicon-heart');
});
</script>

<!-- Modal Forms -->
<div id="formModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="formModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button id="modalclose" type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="contactModalLab">聯絡我們</h4>
            </div>
            <div class="modal-body">
                <form class="form-horizontal" name="postform" method="post" id="postform" enctype="multipart/form-data" >
                    <fieldset>
                                                <div class="form-group" id="qqskype">
                            <label class="col-sm-4 control-label" for="contact">QQ / Skype</label>
                            <div class="col-sm-6">
                                <input id="contact" name="contact" type="text" placeholder="" class="form-control">
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-4 control-label" for="mail">Email</label>
                            <div class="col-sm-6">
                                <input id="mail" name="mail" type="text" placeholder="" class="form-control">
                            </div>
                        </div>
                        <div class="form-group" id="translanguage">
                            <label class="col-sm-4 control-label" for="trans">Your Language</label>
                            <div class="col-sm-6">
                                <input id="trans" name="trans" type="text" placeholder="" class="form-control">
                            </div>
                        </div>
                        <div class="form-group" id="mailcontent">
                            <label class="col-sm-4 control-label" for="intention" id="inten-trans">內容</label>
                            <div class="col-sm-6">
                                <textarea id="intention" name="intention" rows="9" class="form-control"></textarea>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-4 control-label" for="verify">驗證碼</label>
                            <div class="col-sm-6">
                                <input type="text" id="verifycode" name="verifycode" style="width:50px"/>
                                <img id="verify" src="" style="cursor: pointer; vertical-align:middle;" onclick="getverifycode()"/>
                            </div>
                        </div>
                        <input type="hidden" id="adstype" name="adstype" value="1" />
                    </fieldset>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" button class="btn btn-primary" onclick="checkform()">送出</button>
                <button type="button" button class="btn btn-default" data-dismiss="modal">關閉</button>
            </div>
        </div>
    </div>
</div>


<!-- ////////////////////////////////////////////////// -->
<div class="overlay overlay-contentscale">
    <div class="row">
        <div class="col-xs-12 text-center ptb20">
                 <div class="input-group col-xs-offset-2 col-xs-8">
                      <input id="search-input-mobile" type="text" class="form-control" placeholder="搜尋 識別碼, 影片, 演員">
                      <span class="input-group-btn">
                      <button class="btn btn-default" type="submit" onClick="searchs('search-input-mobile')">搜尋</button>
                      </span>
                 </div>
        </div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/">有碼</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/uncensored">無碼</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/genre">有碼類別</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/uncensored/genre">無碼類別</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/actresses">有碼女優</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/uncensored/actresses">無碼女優</a></div>
		<div class="col-xs-6 text-center"><a href="https://www.javbus.org/">歐美</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/genre/hd">高清</a></li></div>
    
       <div class="col-xs-12 text-center overlay-close">
          <i class="glyphicon glyphicon-remove"></i>
       </div>
    </div>
</div>
<script src='https://www.javbus.com/js/nav.overlay.js?v=10.30.3'></script>


</body>
</html>
"""

rst = re.search(r'.*?var gid = (.*?);.*?', text_tmp).groups()[0]
print(rst)
