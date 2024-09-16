import dateparser


class DateStandardizationPipeline:
    def process_item(self, item, spider):
        # raw_date = item['date']  # Assume the scraped date is in `item['date']`

        # Parse the raw date using dateparser
        parsed_date = dateparser.parse("3 weeks ago")

        if parsed_date:
            # Standardize the date to your preferred format (e.g., YYYY-MM-DD)
            item['date'] = parsed_date.strftime('%Y-%m-%d')
        else:
            # Handle case where the date couldn't be parsed (optional)
            item['date'] = None

        return item


parsed_date = dateparser.parse("August 30, 2024")

print(parsed_date.strftime('%Y-%m-%d'))
