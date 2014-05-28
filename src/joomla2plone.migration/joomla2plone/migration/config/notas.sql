#SELECT jos_weblinks.id, jos_weblinks.title, jos_weblinks.alias, jos_weblinks.url, jos_weblinks.description, jos_weblinks.sid, jos_categories.title AS category
#FROM `jos_weblinks`, `jos_categories`
#WHERE jos_weblinks.id=7
#AND jos_weblinks.catid=jos_categories.id

#SELECT jos_weblinks.id, jos_weblinks.title, jos_weblinks.alias, jos_weblinks.url, jos_weblinks.description, jos_categories.title AS category, jos_sections.title as section
#FROM `jos_weblinks`, `jos_categories`, `jos_sections`
#WHERE jos_weblinks.id=7
#AND jos_weblinks.catid=jos_categories.id
#AND jos_weblinks.sid=jos_sections.id

SELECT jos_content.id, jos_content.catid AS category_id, jos_categories.title AS category
FROM `jos_content`, `jos_categories`
WHERE jos_content.id=46
AND jos_content.catid=jos_categories.id

SELECT jos_content.id, jos_sections.title
FROM `jos_content`, `jos_sections`
WHERE jos_content.id=46
AND jos_content.sectionid=jos_sections.id

SELECT jos_content.title as article, jos_categories.title AS category, jos_sections.title as section
FROM `jos_content`, `jos_categories`, `jos_sections`
WHERE jos_content.id=46
AND jos_content.catid=jos_categories.id
AND jos_content.sectionid=jos_sections.id

    SELECT
        ${settings:prefix_db}_content.alias as _id,
        ${settings:prefix_db}_content.title,
        ${settings:prefix_db}_content.introtext as description,
        ${settings:prefix_db}_content.fulltext as text,
        ${settings:prefix_db}_content.metakey as subject_keywords,
        FROM_UNIXTIME(${settings:prefix_db}_content.created, "${settings:date_format}") as creation_date,
        FROM_UNIXTIME(${settings:prefix_db}_content.created, "${settings:date_format}") as effectiveDate,
        FROM_UNIXTIME(${settings:prefix_db}_content.modified, "${settings:date_format}") as modification_date,
        ${settings:prefix_db}_content.state as _status
    FROM ${settings:prefix_db}_content, ${settings:prefix_db}_categories
    WHERE ${settings:prefix_db}_content.id=46
    AND ${settings:prefix_db}_content.catid=34
    GROUP BY
        ${settings:prefix_db}_content.alias,
        ${settings:prefix_db}_content.title,
        ${settings:prefix_db}_content.introtext,
        ${settings:prefix_db}_content.fulltext,
        ${settings:prefix_db}_content.created,
        ${settings:prefix_db}_content.modified,
        ${settings:prefix_db}_content.state;


    SELECT
        jos_content.alias as _id,
        jos_content.title,
        jos_content.introtext as description,
        jos_content.fulltext as text,
        jos_content.metakey as subject_keywords,
        FROM_UNIXTIME(jos_content.created, "%%Y/%%m/%%d %%k:%%i:%%s") as creation_date,
        FROM_UNIXTIME(jos_content.created, "%%Y/%%m/%%d %%k:%%i:%%s") as effectiveDate,
        FROM_UNIXTIME(jos_content.modified, "%%Y/%%m/%%d %%k:%%i:%%s") as modification_date,
        jos_content.state as _status,
        jos_sections.alias as _path
    FROM jos_content, jos_sections
    WHERE jos_content.id=46
    AND jos_content.sectionid=jos_sections.id
    GROUP BY
        jos_content.alias,
        jos_content.title,
        jos_content.introtext,
        jos_content.fulltext,
        jos_content.created,
        jos_content.modified,
        jos_content.state
    ORDER BY
        jos_sections.alias;

#-- newsfeeds
# --http://pypi.python.org/pypi/iservices.rssdocument/0.5.0
SELECT `id`, `alias`, `name`, `link`, `numarticles`, `cache_time`, `checked_out_time`, `published`
FROM `jos_newsfeeds`
WHERE 1
ORDER BY id ASC;


##SELECT * FROM `jos_polls` WHERE 1
SELECT `alias`, `title`, `published` FROM `jos_polls` WHERE 1
ORDER BY `id`

SELECT `pollid`, `id`, `text`, `hits`  FROM `jos_poll_data` WHERE 1
ORDER BY `id`

SELECT `id`, `date`, `vote_id`, `poll_id` FROM `jos_poll_date` WHERE 1

    SELECT
        jos_polls.alias AS _id,
        jos_polls.title AS form-widgets-IBasic-title,
        jos_poll_data.text AS option_data,
        jos_poll_date.date,
        jos_polls.published AS _status
    FROM jos_polls, jos_poll_data, jos_poll_date
    WHERE jos_polls.id=14
    AND jos_poll_data.pollid = jos_polls.id
    AND jos_poll_date.poll_id = jos_polls.id
    GROUP BY
        jos_polls.alias,
        jos_poll_data.text,
        jos_poll_date.date,
        jos_polls.published,
        jos_polls.title
    ORDER BY jos_polls.id ASC
