/**
 * Created by aix on 2015/3/14
 * 基于bootstrap
 * 需要include alert.html模版，以及引入该js文件和alert.css
 */

;(function(window,$){
	//覆盖掉默认的alert，以便自定义且不会阻塞浏览器
	window.alert = function(msg){
		console.log(msg);
		$('#alert_win').modal().find('.modal-body').html(msg);
	};
	//toast，默认2秒后消失
	window.toast = function(msg){
		var $this = $('.toast-content');
		$this.find('.msg-content').html(msg);
		$this.fadeIn('slow');
		window.setTimeout(function(){
			$this.fadeOut();
		},2000);
	}
})(window,$);