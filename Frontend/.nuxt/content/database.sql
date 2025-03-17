CREATE TABLE IF NOT EXISTS _content_info (id TEXT PRIMARY KEY, "ready" BOOLEAN, "structureVersion" VARCHAR, "version" VARCHAR, "__hash__" TEXT UNIQUE); -- structure
INSERT INTO _content_info VALUES ('checksum_content', false, 'DjRIbndRGL', 'v3.3.0--DjRIbndRGL', 'zIiowBmK6D'); -- meta
DROP TABLE IF EXISTS _content_content; -- structure
CREATE TABLE IF NOT EXISTS _content_content (id TEXT PRIMARY KEY, "title" VARCHAR, "body" TEXT, "description" VARCHAR, "extension" VARCHAR, "meta" TEXT, "navigation" TEXT DEFAULT true, "path" VARCHAR, "seo" TEXT DEFAULT '{}', "stem" VARCHAR, "__hash__" TEXT UNIQUE); -- structure
UPDATE _content_info SET ready = true WHERE id = 'checksum_content'; -- meta