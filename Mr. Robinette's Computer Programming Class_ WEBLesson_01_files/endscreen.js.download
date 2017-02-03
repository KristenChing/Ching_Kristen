(function(g){var window=this;var bta=function(a,b){g.U(a).experiments.g("player_gel_logging")&&a.app.V.Lb("onLogToGel",{payload_name:"thumbnailLoaded",payload:b})},cta=function(a,b,c,d){var e=b.Sb();
g.O(a.element,"ytp-suggestion-set",!!e.videoId);var f=b.Jh();d=b.fd(c,d?d:"mqdefault.jpg");var k=b instanceof g.$s?g.kv(b.lengthSeconds):null,l=!!f,f=l&&"RD"==g.zt(f).type;c={title:b.title,author:b.author,author_and_views:e.shortViewCount?b.author+" \u2022 "+e.shortViewCount:b.author,watch:g.P("YTP_WATCH_VIDEO_OR_PLAYLIST",{TITLE:b.title},b.title),duration:k,url:b.xk(c),is_list:l,is_mix:f,background:d?"background-image: url("+d+")":""};b instanceof g.Ct&&(c.playlist_length=b.B);a.update(c)},Q8=function(a){var b=
g.U(a),c=b.experiments.g("video_wall_moving_thumbnails_hover"),c=b.experiments.g("video_wall_moving_thumbnails_autoplay")||c;
this.C=b.C&&!b.J;var d=g.yi||g.rc?{style:"will-change: opacity"}:null,e=["ytp-videowall-still"];b.experiments.g("video_wall_show_text")&&e.push("ytp-show-text");b={K:"img",Z:"ytp-videowall-moving-thumbnail",Y:{src:"{{moving_thumbnail}}"}};g.V.call(this,{K:"a",ea:e,Y:{href:"{{url}}",target:this.C?"_blank":null,"aria-label":"{{watch}}","data-is-list":"{{is_list}}","data-is-mix":"{{is_mix}}"},T:[{K:"div",Z:"ytp-videowall-still-image",Y:{style:"{{background}}"}},c?b:null,{K:"span",Z:"ytp-videowall-still-info",
T:[{K:"span",Z:"ytp-videowall-still-info-bg",T:[{K:"span",Z:"ytp-videowall-still-info-content",Y:d,T:[{K:"span",Z:"ytp-videowall-still-info-title",T:["{{title}}"]},{K:"span",Z:"ytp-videowall-still-info-author",T:["{{author_and_views}}"]},{K:"span",Z:"ytp-videowall-still-info-duration",T:["{{duration}}"]}]}]}]},{K:"span",ea:["ytp-videowall-still-listlabel-regular","ytp-videowall-still-listlabel"],T:[{K:"span",Z:"ytp-videowall-still-listlabel-icon"},g.P("YTP_PLAYLIST"),{K:"span",Z:"ytp-videowall-still-listlabel-length",
T:[" (",{K:"span",T:["{{playlist_length}}"]},")"]}]},{K:"span",ea:["ytp-videowall-still-listlabel-mix","ytp-videowall-still-listlabel"],T:[{K:"span",Z:"ytp-videowall-still-listlabel-mix-icon"},g.P("YTP_MIX"),{K:"span",Z:"ytp-videowall-still-listlabel-length",T:[" (50+)"]}]}]});this.o=a;this.A=null;this.D=0;this.S("click",this.hN);this.S("keypress",this.iN);c&&this.U(this.ua["ytp-videowall-moving-thumbnail"],"load",this.kN);g.U(a).experiments.g("player_interaction_logging")&&(a=a.app.ca,g.eb(a.B,this),
b=String(a.G++),this.element.setAttribute("data-visual-id",b),g.Db(this,(0,g.z)(a.D,a,this)))},dta=function(a){if(5E5<g.Hr(g.U(a.o).D)){var b=a.A.rk();
b&&(a.D=(0,g.xl)(),a.update({moving_thumbnail:b}))}},R8=function(a){g.zv.call(this,a,{K:"div",
ea:["ytp-thumbnail-overlay","ytp-channel-overlay"],T:[{K:"div",Z:"ytp-thumbnail-overlay-image",Y:{style:"{{background}}"}},{K:"div",Z:"ytp-thumbnail-overlay-curtain"}]})},S8=function(a){var b=g.U(a).experiments.g("moving_thumbnails_autonav"),c={K:"img",
Z:"ytp-upnext-moving-thumbnail",Y:{src:"{{moving_thumbnail}}"}},c={K:"div",Z:"ytp-upnext",Y:{"aria-label":"{{watch}}"},T:[{K:"div",Z:"ytp-thumbnail-overlay-image",Y:{style:"{{background}}"}},b?c:null,{K:"div",Z:"ytp-thumbnail-overlay-curtain"},{K:"span",Z:"ytp-upnext-top",T:[{K:"span",Z:"ytp-upnext-header",T:[g.P("YTP_PLAYLIST_UP_NEXT")]},{K:"span",Z:"ytp-upnext-title",T:["{{title}}"]},{K:"span",Z:"ytp-upnext-author",T:["{{author}}"]}]},{K:"a",Z:"ytp-upnext-autoplay-icon",Y:{href:"{{url}}"},T:[{K:"svg",
Y:{height:"100%",version:"1.1",viewBox:"0 0 98 98",width:"100%"},T:[{K:"circle",Z:"ytp-svg-autoplay-circle",Y:{cx:"49",cy:"49",fill:"#000","fill-opacity":"0.8",r:"48"}},{K:"circle",Z:"ytp-svg-autoplay-ring",Y:{cx:"-49",cy:"49","fill-opacity":"0",r:"46.5",stroke:"#FFFFFF","stroke-dasharray":"293","stroke-dashoffset":"-293","stroke-width":"4",transform:"rotate(-90)"}},{K:"polygon",Z:"ytp-svg-autoplay-triangle",Y:{fill:"#fff",points:"32,27 72,49 32,71"}}]}]},{K:"span",Z:"ytp-upnext-bottom",T:[{K:"span",
Z:"ytp-upnext-cancel"},{K:"span",Z:"ytp-upnext-paused",T:[g.P("YTP_AUTOPLAY_PAUSED_2")]}]},{K:"span",Z:"ytp-upnext-close"}]};g.V.call(this,c);this.D=null;var d=this.ua["ytp-upnext-cancel"],c=this.ua["ytp-upnext-close"];this.D=new g.V({K:"button",ea:["ytp-upnext-cancel-button","ytp-button"],Y:{tabindex:0,"aria-label":g.P("YTP_AUTOPLAY_CANCEL")},T:[g.P("YTP_CANCEL")]});g.J(this,this.D);this.D.S("click",this.Su,this);this.D.Ha(d);d=new g.V({K:"button",ea:["ytp-upnext-close-button","ytp-button"]});g.J(this,
d);d.S("click",this.Su,this);d.Ha(c);this.o=a;this.L=this.ua["ytp-svg-autoplay-ring"];this.F=this.C=this.A=this.B=null;this.G=new g.Ld(this.$j,5E3,this);g.J(this,this.G);this.H=0;this.U(this.ua["ytp-upnext-autoplay-icon"],"click",this.YH);this.Pu();this.U(a,"autonavvisibility",this.Pu);this.U(a,"mdxnowautoplaying",this.pH);this.U(a,"mdxautoplaycanceled",this.qH);this.U(a,"mdxautoplayupnext",this.Mw);3==this.o.Xa()&&(a=(a=g.Vl(g.Ml(this.o)))?a.WC():null)&&this.Mw(a);b&&(this.J=0,this.U(this.ua["ytp-upnext-moving-thumbnail"],
"load",this.YO))},eta=function(a,b){a.B=b;
cta(a,b,g.U(a.o),"hqdefault.jpg");g.kh(a.element,"ytp-moving-thumbnail-loaded");a.update({moving_thumbnail:"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"});if(5E5<g.Hr(g.U(a.o).D)){var c=a.B.rk();c&&(a.J=(0,g.xl)(),a.update({moving_thumbnail:c}))}},T8=function(a,b){a.A||(g.Ki("a11y-announce",g.P("YTP_PLAYLIST_UP_NEXT")+" "+a.B.title),a.H=(0,g.xl)(),a.A=new g.Ld((0,g.z)(a.Gm,a,b),25),a.Gm(b));
g.kh(a.element,"ytp-upnext-autoplay-paused")},V8=function(a){U8(a);
a.H=(0,g.xl)();a.Gm();g.N(a.element,"ytp-upnext-autoplay-paused")},U8=function(a){a.A&&(a.A.dispose(),a.A=null)},W8=function(a,b){g.jv.call(this,{K:"div",
ea:["html5-endscreen","ytp-player-content",b||"base-endscreen"]});this.o=a;this.V=!1},fta=function(a){a=g.U(a);
return a.Zb&&!a.za},X8=function(a,b){W8.call(this,a,"videowall-endscreen");
this.ba=a;this.ca=b;this.G=0;this.A=[];this.H=this.D=this.C=null;this.J=this.$=!1;this.F=new g.Qn(this);g.J(this,this.F);this.N=new g.Ld(g.va(g.N,this.element,"ytp-show-tiles"),0);g.J(this,this.N);var c=new g.V({K:"button",ea:["ytp-button","ytp-endscreen-previous"],Y:{"aria-label":g.P("YTP_PREVIOUS")},T:[g.Eg()]});g.J(this,c);c.Ha(this.element);c.S("click",this.fN,this);this.P=new g.lu({K:"div",Z:"ytp-endscreen-content"});g.J(this,this.P);this.P.Ha(this.element);c=new g.V({K:"button",ea:["ytp-button",
"ytp-endscreen-next"],Y:{"aria-label":g.P("YTP_NEXT")},T:[g.Fg()]});g.J(this,c);c.Ha(this.element);c.S("click",this.eN,this);this.B=new S8(a);g.J(this,this.B);g.tm(this.o,this.B.element,5);this.ma()},gta=function(a){return(0,g.Q)(a.N,function(a){return g.mv(a)})},hta=function(a,b,c){return 0==b&&a.C.length&&(b=c/X8.g,2<=c/X8.g&&2<=b&&g.U(a.o).experiments.g("video_wall_emphasize_first"))?2*X8.g:X8.g},Y8=function(a){var b=a.ca.Op();
b!=a.$&&(a.$=b,a.o.Ra("autonavvisibility"))},Z8=function(a){W8.call(this,a,"subscribecard-endscreen");
var b=a.getVideoData();this.A=new R8(a);g.J(this,this.A);g.tm(this.o,this.A.element,5);this.B=new g.V(["div","ytp-subscribe-card",["img","ytp-author-image",{src:b.profilePicture}],["div","ytp-subscribe-card-right",["div","ytp-author-name",b.author],["div","html5-subscribe-button-container"]]]);g.J(this,this.B);this.B.Ha(this.element);this.C=new g.uu(g.P("YTP_SUBSCRIBE"),g.P("YTP_UNSUBSCRIBE"),!0,b.Vq,b.subscribed,"trailer-endscreen",null,a);g.J(this,this.C);this.C.Ha(this.B.ua["html5-subscribe-button-container"]);
this.ma()},$8=function(a){g.ju.call(this,a);
g.Fh({});this.o=null;this.isAvailable=!0;this.A=new g.Qn(this);g.J(this,this.A);this.B=g.U(a);fta(a)?this.o=new X8(this.g,this):this.B.za?this.o=new Z8(this.g):this.o=new W8(this.g);g.J(this,this.o);g.tm(this.g,this.o.element,5);this.Vv();this.A.U(a,"videodatachange",this.Vv,this);this.A.U(a,"crn_endscreen",this.JM,this);this.A.U(a,"crx_endscreen",this.KM,this)};
g.B(Q8,g.V);g.h=Q8.prototype;g.h.yh=function(){var a=this.A.Sb().videoId;g.E2(this.o.app,a,this.A.hd,this.A.Jh(),void 0,void 0)};
g.h.hN=function(a){g.xm(this.o,this);g.ov(a,this.o,!this.o.isFullscreen()&&this.C,this.A.hd||void 0)&&this.yh()};
g.h.jN=function(){this.Da(this.B);this.B=null;dta(this)};
g.h.iN=function(a){switch(a.keyCode){case 13:case 32:g.Nk(a)||(this.yh(),g.Mk(a))}};
g.h.kN=function(a){120<g.Ik(a).naturalWidth&&(g.N(this.element,"ytp-videowall-moving-thumbnail-loaded"),this.A.videoId&&bta(this.o,{isMovingThumbnail:!0,durationLoadingMs:Math.round((0,g.xl)()-this.D),videoId:this.A.videoId}))};
g.B(R8,g.zv);R8.prototype.Cb=function(a){a?this.B.show():g.yv(this.B)};
g.B(S8,g.V);g.h=S8.prototype;g.h.$j=function(){this.C&&(this.G.stop(),this.Da(this.F),this.F=null,this.C.close(),this.C=null)};
g.h.Pu=function(){this.Cb(g.Nl(this.o))};
g.h.OH=function(){window.focus();this.$j()};
g.h.Gm=function(a){a=a||g.U(this.o).experiments.o("autoplay_time")||1E4;var b=Math.min((0,g.xl)()-this.H,a);a=Math.min(b/a,1);this.L.setAttribute("stroke-dashoffset",-293*(a+1));1<=a&&3!=this.o.Xa()?this.select(!0):this.A&&this.A.start()};
g.h.select=function(a){var b=g.U(this.o);if(b.experiments.g("autonav_notifications")&&a&&window.Notification&&window.document.hasFocus){var c=window.Notification.permission;g.em(this.o,"xwebnotifications",{permission:c});"default"==c?window.Notification.requestPermission():"granted"!=c||window.document.hasFocus()||(c=this.B.Sb(),this.$j(),this.C=new window.Notification(g.P("YTP_PLAYLIST_UP_NEXT"),{body:c.title,icon:c.fd(b)}),this.F=this.U(this.C,"click",this.OH),this.G.start())}U8(this);this.o.oj(!1,
a)};
g.h.YH=function(a){!g.cf(this.D.element,g.Ik(a))&&g.ov(a,this.o)&&this.select()};
g.h.Su=function(){g.fm(this.o,"autonavcancel");g.Ql(this.o,!0)};
g.h.YO=function(a){120<g.Ik(a).naturalWidth&&(g.N(this.element,"ytp-moving-thumbnail-loaded"),bta(this.o,{isMovingThumbnail:!0,durationLoadingMs:Math.round((0,g.xl)()-this.J),videoId:this.B.Sb().videoId}))};
g.h.pH=function(a){this.show();T8(this,a)};
g.h.Mw=function(a){this.B&&this.B.Sb().videoId==a.Sb().videoId||eta(this,a)};
g.h.qH=function(){U8(this);this.ma()};
g.h.R=function(){U8(this);this.$j();S8.M.R.call(this)};
g.B(W8,g.jv);W8.prototype.create=function(){this.V=!0};
W8.prototype.destroy=function(){this.V=!1};
W8.prototype.Lm=function(){return!1};
g.B(X8,W8);X8.g=2;g.h=X8.prototype;g.h.create=function(){X8.M.create.call(this);var a=this.o.getVideoData();a&&(this.C=gta(a),this.D=a);this.$f();this.F.U(this.o,"appresize",this.$f);this.F.U(this.o,"videodatachange",this.gN);this.F.U(this.o,"autonavchange",this.by);this.F.U(this.o,"autonavcancel",this.dN);this.F.U(this.element,"transitionend",this.aJ)};
g.h.destroy=function(){g.Sn(this.F);g.Fb(this.A);this.A=[];this.C=null;X8.M.destroy.call(this);g.kh(this.element,"ytp-show-tiles");this.N.stop()};
g.h.Lm=function(){return 1!=this.D.autonavState};
g.h.aj=function(){return g.um(this.o)&&this.Lm()&&!this.H};
g.h.show=function(){X8.M.show.call(this);g.kh(this.element,"ytp-show-tiles");g.U(this.o).isMobile?g.Md(this.N):this.N.start();(this.J||this.H&&this.H!=this.D.clientPlaybackNonce)&&g.Ql(this.o,!1);var a=this.aj();g.um(this.o)&&g.U(this.o).experiments.g("ui_logging")&&this.ca.log({cancelButtonShow:a?"1":"0",state:this.Lm()?"enabled":"disabled"});a?(Y8(this),2==this.D.autonavState?g.U(this.o).experiments.g("fast_autonav_in_background")&&3==this.o.Fx()?this.B.select(!0):T8(this.B):3==this.D.autonavState&&
V8(this.B)):(g.Ql(this.o,!0),Y8(this))};
g.h.ma=function(){X8.M.ma.call(this);V8(this.B);Y8(this)};
g.h.aJ=function(a){g.Ik(a)==this.element&&this.$f()};
g.h.$f=function(){if(this.C&&this.C.length){var a=g.U(this.o).experiments.g("video_wall_moving_thumbnails_hover");g.N(this.element,"ytp-endscreen-paginate");var b=g.nk(this.element),c=b.width/b.height,d=96/54,e=X8.g,f=X8.g,k=Math.max(b.width/96,2),l=Math.max(b.height/54,2),m=this.C.length,n=Math.pow(X8.g,2),q,t=hta(this,0,l),v=hta(this,1,l);q=m*n+(Math.pow(t,2)-n);q+=Math.pow(v,2)-n;for(q-=n;0<q&&(e<k||f<l);){var x=e/X8.g,A=f/X8.g,G=e<=k-X8.g&&q>=A*n,I=f<=l-X8.g&&q>=x*n;if((x+1)/A*d/c>c/(x/(A+1)*
d)&&I)q-=x*n,f+=X8.g;else if(G)q-=A*n,e+=X8.g;else if(I)q-=x*n,f+=X8.g;else break}d=!1;k=X8.g+t;q>=3*n&&6>=m*n-q&&(f>=k||e>=k)&&v<=X8.g&&(d=!0);q=96*e;n=54*f;c=q/n<c?b.height/n:b.width/q;c=Math.min(c,2);q*=c;n*=c;q*=g.oe(b.width/q||1,1,1.21);n*=g.oe(b.height/n||1,1,1.21);q=Math.floor(Math.min(b.width,q));n=Math.floor(Math.min(b.height,n));b=this.P.element;g.mk(b,q,n);g.Vj(b,{marginLeft:q/-2+"px",marginTop:n/-2+"px"});eta(this.B,this.C[0]);g.O(this.element,"ytp-endscreen-takeover",this.aj());Y8(this);
c=q+4;q=n+4;n=0;k=!this.aj();l=!1;for(x=0;x<e;x++)for(A=0;A<f;A++){var I=v>X8.g&&1<=n&&!l?n+1:n,K=0;d&&x>=e-X8.g&&A>=f-X8.g?K=1:0==A%X8.g&&0==x%X8.g&&(A<t&&x<t?0==A&&0==x&&(K=t):v>X8.g&&A>=f-v&&x>=e-v?A==f-v&&x==e-v&&(l=!0,I=1,K=v):K=X8.g);I=g.pe(I+this.G,m);if(0!=K){G=this.A[n];G||(G=new Q8(this.o),this.A[n]=G,b.appendChild(G.element));var $a=Math.floor(q*A/f),sb=Math.floor(c*x/e),nb=Math.floor(q*(A+K)/f)-$a-4,Jd=Math.floor(c*(x+K)/e)-sb-4;g.bk(G.element,sb,$a);g.mk(G.element,Jd,nb);g.Vj(G.element,
"transitionDelay",(A+x)/20+"s");g.O(G.element,"ytp-videowall-still-mini",1==K);g.O(G.element,"ytp-videowall-still-large",2<K);I=this.C[I];K=k&&!a;G.A=I;$a=g.U(G.o);cta(G,I,$a,g.ih(G.element,"ytp-videowall-still-large")?"hqdefault.jpg":"mqdefault.jpg");g.kh(G.element,"ytp-videowall-moving-thumbnail-loaded");G.update({moving_thumbnail:"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"});K?(g.N(G.element,"ytp-videowall-active"),dta(G)):$a.experiments.g("video_wall_moving_thumbnails_hover")&&
!G.B&&(G.B=G.S("mouseover",G.jN));K=I.hd;I=G.o;g.U(I).experiments.g("player_interaction_logging")&&(I=I.app.ca,K=K&&K.itct,G=G.element.getAttribute("data-visual-id"),g.vm(I,"onLogServerVeCreated",{id:G,tracking_params:K}));n++}}g.O(this.element,"ytp-endscreen-paginate",n<m);for(a=this.A.length-1;a>=n;a--)G=this.A[a],g.We(G.element),g.Eb(G);this.A.length=n}};
X8.A=2;X8.o=1.21;g.h=X8.prototype;g.h.gN=function(){var a=this.o.getVideoData();this.D!=a&&(this.G=0,this.C=gta(a),this.D=a,this.$f())};
g.h.eN=function(){this.G+=this.A.length;this.$f()};
g.h.fN=function(){this.G-=this.A.length;this.$f()};
g.h.VE=function(){return!!this.B.A};
g.h.by=function(a){1==a?(this.J=!1,this.H=this.D.clientPlaybackNonce,U8(this.B),this.g&&this.$f()):(this.J=!0,this.g&&this.aj()&&(2==a?T8(this.B):3==a&&V8(this.B)))};
g.h.dN=function(a){if(a){for(a=0;a<this.A.length;a++)g.ym(this.ba,this.A[a],!0);this.by(1)}else this.H=null,this.J=!1;this.$f()};
g.B(Z8,W8);Z8.prototype.show=function(){Z8.M.show.call(this);this.A.Cb(!0)};
Z8.prototype.ma=function(){Z8.M.ma.call(this);this.A.Cb(!1)};
g.B($8,g.ju);g.h=$8.prototype;g.h.Wx=function(){var a=this.g.getVideoData(),b=!fta(this.g)||!(!a.N||!a.N.length),a=g.Ol(a,"ypc_module"),c=g.m_(this.g.app);return(b||!1)&&!a&&!c};
g.h.Op=function(){return(this.o instanceof X8||!1)&&this.o.g&&this.o.aj()};
g.h.SE=function(){return this.Op()?this.o.VE():!1};
g.h.R=function(){g.qm(this.g,"endscreen");$8.M.R.call(this)};
g.h.load=function(){$8.M.load.call(this);this.o.show();g.U(this.g).za&&.01>Math.random()&&this.log({trailerEndscreenShow:1})};
g.h.log=function(a){g.em(this.g,"end",a)};
g.h.unload=function(){$8.M.unload.call(this);this.o.ma();this.o.destroy();this.isAvailable=!1};
g.h.JM=function(a){this.Wx()&&(this.o.V||this.o.create(),"load"==a.getId()&&this.load())};
g.h.KM=function(a){"load"==a.getId()&&this.loaded&&this.unload()};
g.h.Vv=function(){g.qm(this.g,"endscreen");var a=Math.max(1E3*(this.g.getVideoData().lengthSeconds-10),0),a=new g.Am(a,0x8000000000000,{id:"preload",namespace:"endscreen"}),b=new g.Am(0x8000000000000,0x8000000000000,{id:"load",priority:6,namespace:"endscreen"});g.nm(this.g,[a,b])};
window._exportCheck==g.ya&&g.ka("ytmod.player.endscreen",$8,void 0);})(_yt_player);
