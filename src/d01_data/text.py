radial = 'Radar Charts are a way of comparing multiple quantitative variables.\
    This makes them useful for seeing which variables have similar values or if there are any\
    outliers amongst each variable. Radar Charts are also useful for seeing which variables\
    are scoring high or low within a dataset, making them ideal for displaying performance.\
    Each variable is provided with an axis that starts from the centre. All axes are arranged\
    radially, with equal distances between each other, while maintaining the same scale between\
    all axes. Grid lines that connect from axis-to-axis are often used as a guide. Each variable\
    value is plotted along its individual axis and all the variables in a dataset and connected\
    together to form a polygon.However, there are some major flaws with Radar Charts:\
        Having multiple polygons in one Radar Chart makes it hard to read, confusing and too cluttered.\
        Especially if the polygons are filled in, as the top polygon covers all the other polygons underneath it.\
    Having too many variables creates too many axes and can also make the chart hard to read and complicated. So it\'s \
    good practice to keep Radar Charts simple and limit the number of variables used. Another flaw with Radar Charts is\
    that they\'re not so good for comparing values across each variable. Even with the aid of the spiderweb-like grid guide.\
    Comparing values all on a single straight axis is much easier.'
    
pc = 'This type of visualisation is used for plotting multivariate, numerical data. Parallel Coordinates\
    Plots are ideal for comparing many variables together and seeing the relationships between them.\
    For example, if you had to compare an array of products with the same attributes (comparing computer or cars specs across different models).\
    In a Parallel Coordinates Plot, each variable is given its own axis and all the axes are placed in parallel to each other. Each axis can have\
    a different scale, as each variable works off a different unit of measurement, or all the axes can be normalised to keep all the scales uniform.\
    Values are plotted as a series of lines that connected across all the axes. This means that each line is a collection of points placed on each axis,\
    that have all been connected together. The order the axes are arranged in can impact the way how the reader understands the data. One reason for this\
    is that the relationships between adjacent variables are easier to perceive, then for non-adjacent variables. So re-ordering the axes can help in\
    discovering patterns or correlations across variables. The downside to Parallel Coordinates Plots, is that they can become over-cluttered and therefore,\
    illegible when they\'re very data-dense. The best way to remedy this problem is through interactivity and a technique known as “Brushing”.\
    Brushing highlights a selected line or collection of lines while fading out all the others. This allows you to isolate sections of the plot you\'re\
    interested in while filtering out the noise.'
    
pie = 'Extensively used in presentations and offices, Pie Charts help show proportions and percentages between categories,\
    by dividing a circle into proportional segments. Each arc length represents a proportion of each category, while the full\
    circle represents the total sum of all the data, equal to 100%. Pie Charts are ideal for giving the reader a quick idea of\
    the proportional distribution of the data. However the major downsides to pie charts are:\
            They cannot show more than a few values, because as the number of values shown increases,\
            the size of each segment/slice becomes smaller. This makes them unsuitable for large amounts of data.\
            They take up more space than their alternatives, like a 100% \Stacked Bar Chart for example.\
            Mainly due to their size and for the usual need for a legend. They are not great for making accurate comparisons\
            between groups of Pie Charts. This being that it is harder to distinguish the size of items via area when it is for length.\
    In spite of that, comparing a given category (one slice) within the total of a single Pie Chart, then it can often be more effective.'
    
bubble = 'Heatmaps visualise data through variations in colouring. When applied to a tabular format, Heatmaps are useful for cross-examining\
    multivariate data, through placing variables in the rows and columns and colouring the cells within the table. Heatmaps are good for showing\
    variance across multiple variables, revealing any patterns, displaying whether any variables are similar to each other, and for detecting if\
    any correlations exist in-between them. Typically, all the rows are one category (labels displayed on the left or right side) and all the columns\
    are another category (labels displayed on the top or bottom). The individual rows and columns are divided into the subcategories, which all match\
    up with each other in a matrix. The cells contained within the table either contain colour-coded categorical data or numerical data, that is based\
    on a colour scale. The data contained within a cell is based on the relationship between the two variables in the connecting row and column.\
    A legend is required alongside a Heatmap in order for it to be successfully read. Categorical data is colour-coded, while numerical data requires\
    a colour scale that blends from one colour to another, in order to represent the difference in high and low values. A selection of solid colours\
    can be used to represent multiple value ranges (0-10, 11-20, 21-30, etc) or you can use a gradient scale for a single range (for example 0 - 100)\
    by blending two or more colours together. Because of their reliance on colour to communicate values, Heatmaps are a chart better suited to displaying\
    a more generalised view of numerical data, as it\'s harder to accurately tell the differences between colour shades and to extract specific data points\
    from (unless of course, you include the raw data in the cells). Heatmaps can also be used to show the changes in data over time if one of the rows or\
    columns are set to time intervals. An example of this would be to use a Heatmap to compare the temperature changes across the year in multiple cities,\
    to see where\'s the hottest or coldest places. So the rows could list the cities to compare, the columns contain each month and the cells would contain\
    the temperature values.'
    
line = 'Line Graphs are used to display quantitative values over a continuous interval or time period. A Line Graph is most frequently used to show trends\
    and analyse how the data has changed over time. Line Graphs are drawn by first plotting data points on a Cartesian coordinate grid, then connecting a\
    line between all of these points. Typically, the y-axis has a quantitative value, while the x-axis is a timescale or a sequence of intervals. Negative\
    values can be displayed below the x-axis. The direction of the lines on the graph works as a nice metaphor for the data: an upward slope indicates where\
    values have increased and a downward slope indicates where values have decreased. The line\'s journey across the graph can create patterns that reveal\
    trends in a dataset. When grouped with other lines (other data series), individual lines can be compared to one another. However, avoid using more than\
    3-4 lines per graph, as this makes the chart more cluttered and harder to read. A solution to this is to divide the chart into smaller multiples\
    (have a small Line Graph for each data series).'