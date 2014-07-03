REQUIREMENTS="requirements-dev.txt"
TAG= **
END= **

all: init

bower: dependency
	@echo $(TAG)bower install the components for the system$(TAG)
	bower install
	@echo

copy: bower clean
	@echo $(TAG)Copy all the JavaScript files and Assets to the static folder$(TAG)
	cp bower_components/Countable/Countable.js static/js/vendor/
	cp bower_components/backbone/backbone.js static/js/vendor/
	cp bower_components/bootstrap/dist/js/bootstrap.js static/js/vendor/
	cp bower_components/bootstrap/dist/fonts/* static/fonts/
	cp bower_components/bootstrap/dist/css/bootstrap.css static/css/
	cp bower_components/bootstrap/dist/css/bootstrap-theme.css static/css/
	cp bower_components/fontawesome/css/font-awesome.css static/css/
	cp bower_components/fontawesome/fonts/* static/fonts/
	cp bower_components/lodash/dist/lodash.js static/js/vendor/
	cp bower_components/moment/moment.js static/js/vendor/
	cp bower_components/nprogress/nprogress.js static/js/vendor/
	cp bower_components/nprogress/nprogress.css static/css/
	cp bower_components/validator-js/validator.js static/js/vendor/
	@echo
	
init: copy
	@echo $(TAG)cat all the vendor js files into scripts.js$(TAG)
	cat static/js/vendor/*.js >> static/js/scripts.js
	cp bower_components/jquery/dist/jquery.js static/js/
	uglifyjs -o static/js/scripts.min.js static/js/scripts.js
	uglifyjs -o static/js/jquery.min.js static/js/jquery.js
	@echo

dependency:
	@echo $(TAG)init jw djtu$(TAG)
	@echo

clean:
	@echo $(TAG)Clean the vendor files$(TAG)
	rm -f static/js/vendor/*.js
	rm -f static/js/scripts*
	rm -f static/js/jquery*
	@echo

