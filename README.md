# city-transport

Inspired by [Anvaka's City Roads](https://github.com/anvaka/city-roads)

I wanted to try making a similar implementation in Python for practice.

Some additional features I wanted to include:

1. Include railways and metro transit overlayed over the roads with a different color
2. Include options for preset color customizations (e.g. light mode, dark mode)

Current Issues:

1. Performance Issue for large cities (e.g. Tokyo), need to look into caching implementation or prerendering major cities
2. Implementing Pan and Zoom on loaded SVG files

Next Actions:

1. Look into options for caching or prerendering files, need to check if storing prerendered svg files is best solution, or other format.
2. Add function for recoloring rendered maps with preset light mode and dark mode
3. Explore implementation for pan and zoom on generated maps.
4. Allow for export to png format