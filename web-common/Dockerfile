FROM richarvey/nginx-php-fpm
RUN apk --no-cache add mysql-client mysql php5-pdo_mysql php5-mysql php5 tzdata
# remove error "Access to the script has been denied while reading response header from upstream"
RUN sed -i 's/;security.limit_extensions.*/security.limit_extensions = /' /usr/local/etc/php-fpm.d/www.conf

