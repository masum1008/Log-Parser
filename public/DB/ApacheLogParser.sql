CREATE SCHEMA apechelog;

CREATE TABLE sites (
	id                   int  NOT NULL  AUTO_INCREMENT,
	client_ip            varchar(50)    ,
	domain_name          varchar(100)    ,
	url                 varchar(500)    ,
	filename             varchar(100)    ,
	upload_time          timestamp    ,
	CONSTRAINT pk_sites PRIMARY KEY ( id )
 );


CREATE TABLE apechelog.apache_logs ( 
	id                   int  NOT NULL  AUTO_INCREMENT,
	log_host_name        varchar(100)    ,
	log_ip_address       varchar(100)    ,
	remote_log_name      varchar(100)    ,
	http_authentication_username varchar(100)    ,
	received_time        timestamp    ,
	method_type          varchar(10)    ,
	response_code        varchar(5)    ,
	response_size        varchar(50)    ,
	reference            varchar(100)    ,
	user_agent           varchar(50)    ,
	log_url_path         varchar(500)    ,
	received_byte        varchar(20)    ,
	send_byte            varchar(20)    ,
	site_id              int    ,
	CONSTRAINT pk_apache_logs PRIMARY KEY ( id )
 );


CREATE INDEX idx_apache_logs ON apechelog.apache_logs ( site_id );


CREATE TABLE apechelog.log_formets ( 
	id                   int  NOT NULL  AUTO_INCREMENT,
	`1st`                varchar(20)    ,
	`2nd`                varchar(20)    ,
	`3rd`                varchar(20)    ,
	`4th`                varchar(20)    ,
	`5th`                varchar(20)    ,
	`7th`                varchar(20)    ,
	site_id              int    ,
	CONSTRAINT pk_log_formets PRIMARY KEY ( id )
 );

CREATE INDEX idx_log_formets ON apechelog.log_formets ( site_id ) ;

ALTER TABLE apechelog.apache_logs ADD CONSTRAINT fk_apache_logs_sites FOREIGN KEY ( site_id ) REFERENCES apechelog.sites( id ) ON DELETE cascade ON UPDATE cascade;

ALTER TABLE apechelog.log_formets ADD CONSTRAINT fk_log_formets_sites FOREIGN KEY ( site_id ) REFERENCES apechelog.sites( id ) ON DELETE cascade ON UPDATE cascade;
