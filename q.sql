SELECT article.id, article.title, article.text
FROM article
LEFT OUTER JOIN comment ON article.id = comment.article_id
WHERE comment.id IS NULL;