CREATE DATABASE collab_dev;
CREATE DATABASE kb_dev;
CREATE DATABASE phoenix;

\connect collab_dev
CREATE EXTENSION pgroonga;

\connect kb_dev
CREATE EXTENSION vector;
CREATE EXTENSION pgroonga;
CREATE EXTENSION age;
