CREATE USER project_csi2132 WITH PASSWORD 'project_csi2132';
GRANT ALL PRIVILEGES ON DATABASE "project_database" TO project_csi2132;

COMMENT ON DATABASE "project_database" IS 'Database for the test';
