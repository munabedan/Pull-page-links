import re
import os

def process_text(text, prefix_link):
    # Define regular expression patterns to match href and src attributes
    href_pattern = r'href="([^"]+\.css)"'
    src_pattern = r'src="([^"]+\.js)"'
    image_pattern = r'src="([^"]+\.png)"'

    # Find all matches of the patterns in the text
    href_matches = re.findall(href_pattern, text)
    src_matches = re.findall(src_pattern, text)
    image_matches = re.findall(image_pattern, text)

    # Prefix each link with the given prefix_link
    prefixed_links = [f"{prefix_link}{link}" for link in href_matches + src_matches + image_matches]

    # remove duplicates
    prefixed_links = list(set(prefixed_links))

    return prefixed_links

def download_links(links):
    # Create directories for CSS and JS files
    os.makedirs("css", exist_ok=True)
    os.makedirs("js", exist_ok=True)
    os.makedirs("images", exist_ok=True)

    # Loop through the links and download each one using wget
    for link in links:
        if link.endswith(".css"):
            os.system(f"wget {link} -P css/")
        elif link.endswith(".js"):
            os.system(f"wget {link} -P js/")
        elif link.endswith(".png"):
            os.system(f"wget {link} -P images/")

# Example usage
text = """
<!DOCTYPE html>

<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <link rel="shortcut icon" href="/public/images/favicon.ico">

    <link rel="stylesheet" href="/public/css/screen.css" type="text/css" media="screen">
    <link rel="stylesheet" href="/public/css/colorbox.css" type="text/css" media="screen">
    <link rel="stylesheet" href="/public/css/tipsy.css" type="text/css" media="screen">

    <script src="/public/js/jquery.min.js" type="text/javascript"></script>
    <script src="/public/js/jquery.ui.min.js" type="text/javascript"></script>
    <script src="/public/js/jquery.colorbox.min.js" type="text/javascript"></script>
    <script src="/public/js/jquery.tipsy.js" type="text/javascript"></script>
    <script src="/public/js/ds.js" type="text/javascript"></script>


    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-24042959-1']);
        _gaq.push(['_trackPageview']);

        (function () {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>


    <title>DotShare.it</title>
</head>

<body>

    <div id="header">
        <div id="nav">
            <ul class="label">
                <li><span class="orange">.</span>share</li>
            </ul>

            <ul>
                <li>guest<span class="gray">@</span>dotshare <span class="gray">[</span>~<span class="gray">]</span>
                    <span class="gray">$</span> ls -a nav/</li>

                <li><a href="/">..</a></li>
                <li><a href="/news/">news</a></li>
                <li><a href="/dots/">browse</a></li>



                <li><a href="/about/">about</a></li>




                <li><a href="/login/">login</a></li>
                <li><a href="/register/">register</a></li>

            </ul>
        </div>

        <div id="donate">
            <ul>
                <li><a href="/donate/">donate</a></li>
            </ul>
        </div>
    </div>

    <div id="commands">
        <div id="command">
            <p>
                <span class="dark-gray">guest</span>@<span class="dark-gray">dotshare</span> [<span
                    class="dark-gray">~/groups/wms/awesome</span>] <span class="dark-gray">$</span> ls
            </p>
        </div>
    </div>

    <div id="container">
        <div id="categories">
            <ul>

                <li class="label">
                    chat/

                    <ul>

                        <li><a href="/category/chat/irssi/">irssi</a></li>

                        <li><a href="/category/chat/weechat/">weechat</a></li>

                    </ul>
                </li>

                <li class="label">
                    emacs/

                    <ul>

                        <li><a href="/category/emacs/colors/">colors</a></li>

                        <li><a href="/category/emacs/config/">config</a></li>

                    </ul>
                </li>

                <li class="label">
                    fms/

                    <ul>

                        <li><a href="/category/fms/mc/">mc</a></li>

                        <li><a href="/category/fms/ranger/">ranger</a></li>

                    </ul>
                </li>

                <li class="label">
                    info/

                    <ul>

                        <li><a href="/category/info/conky/">conky</a></li>

                        <li><a href="/category/info/dzen2/">dzen2</a></li>

                    </ul>
                </li>

                <li class="label">
                    misc/

                    <ul>

                        <li><a href="/category/misc/misc/">misc</a></li>

                    </ul>
                </li>

                <li class="label">
                    mpd/

                    <ul>

                        <li><a href="/category/mpd/ncmpcpp/">ncmpcpp</a></li>

                    </ul>
                </li>

                <li class="label">
                    panels/

                    <ul>

                        <li><a href="/category/panels/bmpanel/">bmpanel</a></li>

                        <li><a href="/category/panels/lxpanel/">lxpanel</a></li>

                        <li><a href="/category/panels/pypanel/">pypanel</a></li>

                        <li><a href="/category/panels/tint2/">tint2</a></li>

                    </ul>
                </li>

                <li class="label">
                    shells/

                    <ul>

                        <li><a href="/category/shells/bash/">bash</a></li>

                        <li><a href="/category/shells/tcsh/">tcsh</a></li>

                        <li><a href="/category/shells/zsh/">zsh</a></li>

                    </ul>
                </li>

                <li class="label">
                    terms/

                    <ul>

                        <li><a href="/category/terms/colors/">colors</a></li>

                        <li><a href="/category/terms/screen/">screen</a></li>

                        <li><a href="/category/terms/tmux/">tmux</a></li>

                    </ul>
                </li>

                <li class="label">
                    vim/

                    <ul>

                        <li><a href="/category/vim/colors/">colors</a></li>

                        <li><a href="/category/vim/rc/">rc</a></li>

                    </ul>
                </li>

                <li class="label">
                    wms/

                    <ul>

                        <li><a href="/category/wms/awesome/">awesome</a></li>

                        <li><a href="/category/wms/bspwm/">bspwm</a></li>

                        <li><a href="/category/wms/dwm/">dwm</a></li>

                        <li><a href="/category/wms/fluxbox/">fluxbox</a></li>

                        <li><a href="/category/wms/fvwm/">fvwm</a></li>

                        <li><a href="/category/wms/herbstluft/">herbstluft</a></li>

                        <li><a href="/category/wms/i3/">i3</a></li>

                        <li><a href="/category/wms/monster/">monster</a></li>

                        <li><a href="/category/wms/openbox/">openbox</a></li>

                        <li><a href="/category/wms/ratpoison/">ratpoison</a></li>

                        <li><a href="/category/wms/spectrwm/">spectrwm</a></li>

                        <li><a href="/category/wms/stumpwm/">stumpwm</a></li>

                        <li><a href="/category/wms/subtle/">subtle</a></li>

                        <li><a href="/category/wms/wmfs/">wmfs</a></li>

                        <li><a href="/category/wms/xmonad/">xmonad</a></li>

                    </ul>
                </li>

            </ul>
        </div>

        <div id="content">




            <div class="item">
                <div class="header">
                    <h1>Moar dots!</h1>
                </div>

                <div class="content">

                    <table id="dots">
                        <thead>
                            <tr>

                                <th><a href="/category/wms/awesome/sort/title/">Title</a></th>


                                <th>User</th>


                                <th><a href="/category/wms/awesome/rsort/date/">Date</a></th>



                                <th><a class="likes" href="/category/wms/awesome/sort/likes/"><img
                                            src="/public/images/like.png" width="16" height="16" alt="likes"></a></th>



                                <th><a class="comments" href="/category/wms/awesome/sort/comments/"><img
                                            src="/public/images/comments.png" width="16" height="16" alt="comments"></a>
                                </th>


                                <th>&nbsp;</th>
                            </tr>
                        </thead>

                        <tbody>


                            <tr>
                                <td><a href="/dots/8465/">Simplified awesomewm</a></td>
                                <td><a href="/~linuxkitty/">linuxkitty</a></td>
                                <td>Nov 29, 2020</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8465.png" rel="scrot"
                                        title="Simplified awesomewm:linuxkitty:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8442/">first try</a></td>
                                <td><a href="/~zenobit/">zenobit</a></td>
                                <td>Aug 21, 2020</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8442.jpg" rel="scrot"
                                        title="first try:zenobit:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8393/">dark side</a></td>
                                <td><a href="/~bit6tream/">bit6tream</a></td>
                                <td>Jan 17, 2020</td>
                                <td class="likes">+1</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8393.png" rel="scrot"
                                        title="dark side:bit6tream:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8384/">military style v1.2</a></td>
                                <td><a href="/~paranoid73/">paranoid73</a></td>
                                <td>Sep 09, 2019</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8384.png" rel="scrot"
                                        title="military style v1.2:paranoid73:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8380/">Almost default Awesome</a></td>
                                <td><a href="/~Ogis1975/">Ogis1975</a></td>
                                <td>Aug 19, 2019</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8380.png" rel="scrot"
                                        title="Almost default Awesome:Ogis1975:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8367/">anonymous</a></td>
                                <td><a href="/~szorfein/">szorfein</a></td>
                                <td>May 26, 2019</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8367.jpg" rel="scrot"
                                        title="anonymous:szorfein:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8277/">arch green</a></td>
                                <td><a href="/~paranoid73/">paranoid73</a></td>
                                <td>Mar 10, 2018</td>
                                <td class="likes">+1</td>
                                <td class="comments">4</td>
                                <td>

                                    <a href="/public/images/uploads/8277.png" rel="scrot"
                                        title="arch green:paranoid73:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8258/">senos</a></td>
                                <td><a href="/~senos/">senos</a></td>
                                <td>Feb 01, 2018</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/8258.jpg" rel="scrot"
                                        title="senos:senos:wms:awesome"><img src="/public/images/scrot.png" width="16"
                                            height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/8256/">WPGTK Awesome base</a></td>
                                <td><a href="/~domsch1988/">domsch1988</a></td>
                                <td>Jan 18, 2018</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    &nbsp;

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/1453/">Original Powerarrow</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Mar 03, 2017</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/1453.png" rel="scrot"
                                        title="Original Powerarrow:lukebonham:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/1432/">Vertex</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Jan 30, 2017</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/1432.jpg" rel="scrot"
                                        title="Vertex:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/1421/">Clock widget for Awesome &gt;= 4.0</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Jan 18, 2017</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    &nbsp;

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/1032/">Powerarrow Reder</a></td>
                                <td><a href="/~Serge2702/">Serge2702</a></td>
                                <td>Jul 03, 2015</td>
                                <td class="likes">+2</td>
                                <td class="comments">10</td>
                                <td>

                                    <a href="/public/images/uploads/1032.png" rel="scrot"
                                        title="Powerarrow Reder:Serge2702:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/955/">work-lt_rc.lua</a></td>
                                <td><a href="/~sailyn/">sailyn</a></td>
                                <td>Jan 02, 2015</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    &nbsp;

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/906/">Awesome theme</a></td>
                                <td><a href="/~tpoisot/">tpoisot</a></td>
                                <td>Sep 27, 2014</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    &nbsp;

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/846/">Darkness AWM</a></td>
                                <td><a href="/~arkhan/">arkhan</a></td>
                                <td>Jul 09, 2014</td>
                                <td class="likes">+2</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/846.png" rel="scrot"
                                        title="Darkness AWM:arkhan:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/820/">awesome in void linux</a></td>
                                <td><a href="/~wagmic/">wagmic</a></td>
                                <td>May 26, 2014</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/820.png" rel="scrot"
                                        title="awesome in void linux:wagmic:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/803/">Awesome PowerArrow-Darker</a></td>
                                <td><a href="/~juancamilo2000/">juancamilo2000</a></td>
                                <td>Apr 22, 2014</td>
                                <td class="likes">+2</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/803.png" rel="scrot"
                                        title="Awesome PowerArrow-Darker:juancamilo2000:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/655/">copland</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Sep 20, 2013</td>
                                <td class="likes">+3</td>
                                <td class="comments">3</td>
                                <td>

                                    <a href="/public/images/uploads/655.png" rel="scrot"
                                        title="copland:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/652/">dremora 2.0</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Sep 14, 2013</td>
                                <td class="likes">+3</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/652.png" rel="scrot"
                                        title="dremora 2.0:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/651/">holo 3.0</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Sep 14, 2013</td>
                                <td class="likes">+7</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/651.jpg" rel="scrot"
                                        title="holo 3.0:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/650/">multicolor</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Sep 13, 2013</td>
                                <td class="likes">+4</td>
                                <td class="comments">3</td>
                                <td>

                                    <a href="/public/images/uploads/650.png" rel="scrot"
                                        title="multicolor:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/649/">powerarrow-darker 2.0</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Sep 13, 2013</td>
                                <td class="likes">+4</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/649.jpg" rel="scrot"
                                        title="powerarrow-darker 2.0:lukebonham:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/648/">steamburn</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Sep 13, 2013</td>
                                <td class="likes">+2</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/648.png" rel="scrot"
                                        title="steamburn:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/632/">Clock widget for AwesomeWM 3.5</a></td>
                                <td><a href="/~maisvendoo/">maisvendoo</a></td>
                                <td>Aug 12, 2013</td>
                                <td class="likes">+1</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/632.jpeg" rel="scrot"
                                        title="Clock widget for AwesomeWM 3.5:maisvendoo:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/606/">rainbow</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Jul 26, 2013</td>
                                <td class="likes">+1</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/606.png" rel="scrot"
                                        title="rainbow:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/553/">blackburn</a></td>
                                <td><a href="/~lukebonham/">lukebonham</a></td>
                                <td>Apr 25, 2013</td>
                                <td class="likes">+1</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/553.png" rel="scrot"
                                        title="blackburn:lukebonham:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/533/">Articuno 3.5</a></td>
                                <td><a href="/~alexjj/">alexjj</a></td>
                                <td>Mar 24, 2013</td>
                                <td class="likes">+1</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/533.jpg" rel="scrot"
                                        title="Articuno 3.5:alexjj:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/505/">Azulito</a></td>
                                <td><a href="/~conandoel/">conandoel</a></td>
                                <td>Jan 11, 2013</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/505.png" rel="scrot"
                                        title="Azulito:conandoel:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/501/">Powerline</a></td>
                                <td><a href="/~sidwitherjay/">sidwitherjay</a></td>
                                <td>Jan 04, 2013</td>
                                <td class="likes">+3</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/501.png" rel="scrot"
                                        title="Powerline:sidwitherjay:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/498/">Sort of Nice</a></td>
                                <td><a href="/~kebertx/">kebertx</a></td>
                                <td>Jan 02, 2013</td>
                                <td class="likes">+3</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/498.png" rel="scrot"
                                        title="Sort of Nice:kebertx:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/490/">minimal</a></td>
                                <td><a href="/~dodo/">dodo</a></td>
                                <td>Dec 19, 2012</td>
                                <td class="likes">+3</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/490.png" rel="scrot"
                                        title="minimal:dodo:wms:awesome"><img src="/public/images/scrot.png" width="16"
                                            height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/471/">Think Correctly</a></td>
                                <td><a href="/~ddblue/">ddblue</a></td>
                                <td>Nov 08, 2012</td>
                                <td class="likes">+5</td>
                                <td class="comments">3</td>
                                <td>

                                    <a href="/public/images/uploads/471.png" rel="scrot"
                                        title="Think Correctly:ddblue:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/452/">Cold-Grey</a></td>
                                <td><a href="/~venam/">venam</a></td>
                                <td>Sep 29, 2012</td>
                                <td class="likes">+1</td>
                                <td class="comments">2</td>
                                <td>

                                    <a href="/public/images/uploads/452.png" rel="scrot"
                                        title="Cold-Grey:venam:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/442/">Garish</a></td>
                                <td><a href="/~Him/">Him</a></td>
                                <td>Sep 14, 2012</td>
                                <td class="likes">+6</td>
                                <td class="comments">2</td>
                                <td>

                                    <a href="/public/images/uploads/442.png" rel="scrot"
                                        title="Garish:Him:wms:awesome"><img src="/public/images/scrot.png" width="16"
                                            height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/369/">The Cave</a></td>
                                <td><a href="/~Kanashi/">Kanashi</a></td>
                                <td>Jun 10, 2012</td>
                                <td class="likes">+1</td>
                                <td class="comments">2</td>
                                <td>

                                    <a href="/public/images/uploads/369.png" rel="scrot"
                                        title="The Cave:Kanashi:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/368/">Snow in June</a></td>
                                <td><a href="/~Kanashi/">Kanashi</a></td>
                                <td>Jun 09, 2012</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/368.png" rel="scrot"
                                        title="Snow in June:Kanashi:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/356/">Awesome config</a></td>
                                <td><a href="/~Beastie/">Beastie</a></td>
                                <td>Apr 24, 2012</td>
                                <td class="likes">+1</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/356.png" rel="scrot"
                                        title="Awesome config:Beastie:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/318/">e&#39;s useless theme.lua</a></td>
                                <td><a href="/~erkin/">erkin</a></td>
                                <td>Feb 06, 2012</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    &nbsp;

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/317/">e&#39;s useless rc.lua</a></td>
                                <td><a href="/~erkin/">erkin</a></td>
                                <td>Feb 06, 2012</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    &nbsp;

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/310/">Conscience</a></td>
                                <td><a href="/~unlog1c/">unlog1c</a></td>
                                <td>Feb 04, 2012</td>
                                <td class="likes">+3</td>
                                <td class="comments">5</td>
                                <td>

                                    <a href="/public/images/uploads/310.png" rel="scrot"
                                        title="Conscience:unlog1c:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/287/">Modern</a></td>
                                <td><a href="/~zhuravlik/">zhuravlik</a></td>
                                <td>Dec 08, 2011</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/287.png" rel="scrot"
                                        title="Modern:zhuravlik:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/182/">Tea</a></td>
                                <td><a href="/~Him/">Him</a></td>
                                <td>Jul 31, 2011</td>
                                <td class="likes">+6</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/182.png" rel="scrot"
                                        title="Tea:Him:wms:awesome"><img src="/public/images/scrot.png" width="16"
                                            height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/131/">Bryter Layter</a></td>
                                <td><a href="/~Him/">Him</a></td>
                                <td>Jul 04, 2011</td>
                                <td class="likes">+7</td>
                                <td class="comments">4</td>
                                <td>

                                    <a href="/public/images/uploads/131.png" rel="scrot"
                                        title="Bryter Layter:Him:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/116/">Sweet Tears</a></td>
                                <td><a href="/~ANOKNUSA/">ANOKNUSA</a></td>
                                <td>Jul 02, 2011</td>
                                <td class="likes">+5</td>
                                <td class="comments">2</td>
                                <td>

                                    <a href="/public/images/uploads/116.png" rel="scrot"
                                        title="Sweet Tears:ANOKNUSA:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/94/">Mr. Snail Goes to Town</a></td>
                                <td><a href="/~guff/">guff</a></td>
                                <td>Jun 28, 2011</td>
                                <td class="likes">+2</td>
                                <td class="comments">1</td>
                                <td>

                                    <a href="/public/images/uploads/94.png" rel="scrot"
                                        title="Mr. Snail Goes to Town:guff:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/75/">Come To The Rock Side</a></td>
                                <td><a href="/~SuNjACk/">SuNjACk</a></td>
                                <td>Jun 25, 2011</td>
                                <td class="likes">+10</td>
                                <td class="comments">9</td>
                                <td>

                                    <a href="/public/images/uploads/75.png" rel="scrot"
                                        title="Come To The Rock Side:SuNjACk:wms:awesome"><img
                                            src="/public/images/scrot.png" width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/62/">Narco</a></td>
                                <td><a href="/~ivo/">ivo</a></td>
                                <td>Jun 25, 2011</td>
                                <td class="likes">&nbsp;</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/62.png" rel="scrot"
                                        title="Narco:ivo:wms:awesome"><img src="/public/images/scrot.png" width="16"
                                            height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/61/">The Color Purple</a></td>
                                <td><a href="/~Him/">Him</a></td>
                                <td>Jun 24, 2011</td>
                                <td class="likes">+3</td>
                                <td class="comments">3</td>
                                <td>

                                    <a href="/public/images/uploads/61.png" rel="scrot"
                                        title="The Color Purple:Him:wms:awesome"><img src="/public/images/scrot.png"
                                            width="16" height="16" alt="scrot"></a>

                                </td>
                            </tr>

                            <tr>
                                <td><a href="/dots/15/">Mr. Owl</a></td>
                                <td><a href="/~Him/">Him</a></td>
                                <td>Jun 22, 2011</td>
                                <td class="likes">+2</td>
                                <td class="comments">&nbsp;</td>
                                <td>

                                    <a href="/public/images/uploads/15.png" rel="scrot"
                                        title="Mr. Owl:Him:wms:awesome"><img src="/public/images/scrot.png" width="16"
                                            height="16" alt="scrot"></a>

                                </td>
                            </tr>


                        </tbody>
                    </table>

                </div>
            </div>


            <div id="pages">



                <strong>1</strong>






                <a href="/category/wms/awesome/p/2/">2</a>




            </div>


        </div>

        <div id="footer">&nbsp;</div>
    </div>

    <div id="logo">
        <a href="/"><img src="/public/images/logo.png" width="62" height="63" alt="DotShare.it"></a>
    </div>

</body>

</html>
"""

prefix_link = "http://dotshare.it"

# Process the text to extract links and prefix them with the given link
prefixed_links = process_text(text, prefix_link)

# Download each link using wget and group them in separate folders
download_links(prefixed_links)
