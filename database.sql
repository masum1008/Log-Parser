CREATE DATABASE logs;
USE logs;
CREATE TABLE apache_logs_apachelog
(
  id                         INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  local_ip                   VARCHAR(20)  NULL,
  format_id                  INT          NOT NULL,
  site_id                    INT          NULL,
  status                     INT          NOT NULL,
  response_bytes_clf         VARCHAR(30)  NULL,
  remote_host                VARCHAR(50)  NULL,
  request_method             VARCHAR(4)   NULL,
  request_url_path           VARCHAR(500) NULL,
  time_received_tz_isoformat VARCHAR(50)  NULL,
  time_us                    VARCHAR(50)  NULL,
  time_received_tz           DATETIME     NULL
)
  ENGINE = InnoDB;

CREATE TABLE auth_group
(
  id   INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  CONSTRAINT name
  UNIQUE (name)
)
  ENGINE = InnoDB;

CREATE TABLE auth_group_permissions
(
  id            INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  group_id      INT NOT NULL,
  permission_id INT NOT NULL,
  CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq
  UNIQUE (group_id, permission_id),
  CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
  FOREIGN KEY (group_id) REFERENCES auth_group (id)
)
  ENGINE = InnoDB;

CREATE INDEX auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
  ON auth_group_permissions (permission_id);

CREATE TABLE auth_permission
(
  id              INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  name            VARCHAR(255) NOT NULL,
  content_type_id INT          NOT NULL,
  codename        VARCHAR(100) NOT NULL,
  CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq
  UNIQUE (content_type_id, codename)
)
  ENGINE = InnoDB;

ALTER TABLE auth_group_permissions
  ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
FOREIGN KEY (permission_id) REFERENCES auth_permission (id);

CREATE TABLE auth_user
(
  id           INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  password     VARCHAR(128) NOT NULL,
  last_login   DATETIME     NULL,
  is_superuser TINYINT(1)   NOT NULL,
  username     VARCHAR(150) NOT NULL,
  first_name   VARCHAR(30)  NOT NULL,
  last_name    VARCHAR(30)  NOT NULL,
  email        VARCHAR(254) NOT NULL,
  is_staff     TINYINT(1)   NOT NULL,
  is_active    TINYINT(1)   NOT NULL,
  date_joined  DATETIME     NOT NULL,
  CONSTRAINT username
  UNIQUE (username)
)
  ENGINE = InnoDB;

CREATE TABLE auth_user_groups
(
  id       INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  user_id  INT NOT NULL,
  group_id INT NOT NULL,
  CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq
  UNIQUE (user_id, group_id),
  CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
  FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id
  FOREIGN KEY (group_id) REFERENCES auth_group (id)
)
  ENGINE = InnoDB;

CREATE INDEX auth_user_groups_group_id_97559544_fk_auth_group_id
  ON auth_user_groups (group_id);

CREATE TABLE auth_user_user_permissions
(
  id            INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  user_id       INT NOT NULL,
  permission_id INT NOT NULL,
  CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
  UNIQUE (user_id, permission_id),
  CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
  FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
  FOREIGN KEY (permission_id) REFERENCES auth_permission (id)
)
  ENGINE = InnoDB;

CREATE INDEX auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
  ON auth_user_user_permissions (permission_id);

CREATE TABLE django_admin_log
(
  id              INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  action_time     DATETIME             NOT NULL,
  object_id       LONGTEXT             NULL,
  object_repr     VARCHAR(200)         NOT NULL,
  action_flag     SMALLINT(5) UNSIGNED NOT NULL,
  change_message  LONGTEXT             NOT NULL,
  content_type_id INT                  NULL,
  user_id         INT                  NOT NULL,
  CONSTRAINT django_admin_log_user_id_c564eba6_fk
  FOREIGN KEY (user_id) REFERENCES auth_user (id)
)
  ENGINE = InnoDB;

CREATE INDEX django_admin_log_content_type_id_c4bce8eb_fk_django_co
  ON django_admin_log (content_type_id);

CREATE INDEX django_admin_log_user_id_c564eba6_fk
  ON django_admin_log (user_id);

CREATE TABLE django_content_type
(
  id        INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  app_label VARCHAR(100) NOT NULL,
  model     VARCHAR(100) NOT NULL,
  CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq
  UNIQUE (app_label, model)
)
  ENGINE = InnoDB;

ALTER TABLE auth_permission
  ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co
FOREIGN KEY (content_type_id) REFERENCES django_content_type (id);

ALTER TABLE django_admin_log
  ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co
FOREIGN KEY (content_type_id) REFERENCES django_content_type (id);

CREATE TABLE django_migrations
(
  id      INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  app     VARCHAR(255) NOT NULL,
  name    VARCHAR(255) NOT NULL,
  applied DATETIME     NOT NULL
)
  ENGINE = InnoDB;

CREATE TABLE django_session
(
  session_key  VARCHAR(40) NOT NULL
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  session_data LONGTEXT    NOT NULL,
  expire_date  DATETIME    NOT NULL
)
  ENGINE = InnoDB;

CREATE INDEX django_session_expire_date_a5c62663
  ON django_session (expire_date);

CREATE TABLE log_formats_logformats
(
  id         INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  site_id    INT          NULL,
  log_format VARCHAR(100) NULL,
  is_default INT          NULL
)
  ENGINE = InnoDB;

CREATE INDEX log_formats_logformats_sites_site_id_fk
  ON log_formats_logformats (site_id);

CREATE TABLE sites_site
(
  id        INT AUTO_INCREMENT
  CONSTRAINT `PRIMARY`
  PRIMARY KEY,
  site_name VARCHAR(30)  NULL,
  site_url  VARCHAR(111) NULL
)
  ENGINE = InnoDB;

ALTER TABLE log_formats_logformats
  ADD CONSTRAINT log_formats_logformats_sites_site_id_fk
FOREIGN KEY (site_id) REFERENCES sites_site (id);

