import re

haystack = 'asdfasdfasdf<script src="aasdf">javascr\nipt\nh\ne\nre</script>asdfasdfasdfasdf'

needle = '<script(.|\n)*</script>'

re_match = re.search(needle, haystack)
print(re_match.group(0))
