/*global window, document, $, SVG */

var survivor = survivor || {};

survivor.dashboard = (function () {
    'use strict';

    // Parse an ISO-8601-formatted date string
    function parseDate(s) {
        return new Date(Date.parse(s));
    }

    // Transform an HTML <table> into a two-dimensional array of strings
    function slurp(table) {
        return $.makeArray($(table).find('tbody tr')).map(function (tr) {
            return $.makeArray($(tr).find('td')).map(function (td) {
                return $(td).text();
            });
        });
    }

    // Extract data from each row in the <tbody> of `dataTable`. Each function
    // in `mappers` transforms values in a single column
    function extractData(dataTable, mappers) {
        return slurp(dataTable).map(function (row) {
            return mappers.map(function (mapper, idx) {
                return mapper(row[idx]);
            });
        });
    }

    // ----------------------------------------
    // Charts

    // logical chart units
    var CHART_WIDTH = 1000,
        CHART_HEIGHT = 1000;

    function Chart() {}

    Chart.prototype.init = function (title) {
        var $container = $('<div class="chart-container">');
        var $chart = $('<div class="chart">');

        $container.append('<label>' + title + '</label>');
        $container.append($chart);

        var svg = SVG($chart.get(0), '100%', '100%');
        svg.viewbox(0, 0, CHART_WIDTH, CHART_HEIGHT);
        svg.attr('preserveAspectRatio', 'none');

        this.element = $container.get(0);
        this.svg = svg;
    };

    // A chart that draws an array of column groups, where each column group is
    // an array of numbers in the range [0, 1].
    function ColumnChart(title) {
        return this.init(title);
    }

    ColumnChart.prototype = new Chart();

    ColumnChart.prototype.draw = function (data) {
        var colsPerGroup = data[0].length + 1; // include a spacer column
        var totalCols = data.length * colsPerGroup - 1;
        var colWidth = CHART_WIDTH / totalCols;

        data.forEach(function (row, rowIdx) {
            row.forEach(function (val, colIdx) {
                var colHeight = val * CHART_HEIGHT;
                var hOffset = colWidth * (colsPerGroup * rowIdx + colIdx);
                var vOffset = CHART_HEIGHT - colHeight;
                var col = this.svg.rect(colWidth, colHeight);
                col.attr({ 'x': hOffset,
                           'y': vOffset,
                           'class': 'column-' + colIdx,
                           'stroke-width': 0 });
            }, this);
        }, this);
    };

    // A chart that draws a line chart from an array of values, where each value
    // is a number in the range [0, 1].
    function LineChart(title) {
        return this.init(title);
    }

    LineChart.prototype = new Chart();

    LineChart.prototype.strokeWidth = 10;

    LineChart.prototype.toPoints = function (values) {
        var hOffset = CHART_WIDTH / (values.length - 1);
        var points = values.map(function (val, idx) {
            return { x: hOffset * idx, y: CHART_HEIGHT - val * CHART_HEIGHT };
        });

        // Close the path, allowing for stroke width
        // This extends the chart outside of the visible area so we don't
        // see any weird edges, i.e.:
        //
        //  +---------------------+
        //  |..---................|
        // ++-/   -\.............-++
        // ||       -\.....-----/ ||
        // ||         ----/       ||
        // ||                     ||
        // |+---------------------+|
        // +-----------------------+

        points[0].x -= this.strokeWidth;
        points[points.length - 1].x += this.strokeWidth;
        points.push({ x: CHART_WIDTH + this.strokeWidth, y: CHART_HEIGHT + this.strokeWidth });
        points.push({ x: -this.strokeWidth, y: CHART_HEIGHT + this.strokeWidth });

        return points;
    };

    LineChart.prototype.draw = function (values) {
        var points = this.toPoints(values);
        var pathStr = points.map(function (p) { return p.x + ',' + p.y; }).join(' ');
        var area = this.svg.polygon(pathStr);
        area.attr({ 'class': 'line-chart',
                    'stroke-width': this.strokeWidth });
    };

    // ----------------------------------------
    // Initialisation

    function initBugRateChart(args) {
        var $dataTable = $('#bug-rate-data');

        var data = extractData($dataTable, [parseDate, parseInt, parseInt]);
        var rawValues = data.map(function (group) {
            // drop date; we don't display it
            return group.slice(1);
        });

        // Normalise values into the range [0, 1]
        var max = Math.max.apply(null, rawValues.map(function (group) {
            return Math.max.apply(null, group);
        }));
        var relativeValues = rawValues.map(function (group) {
            return group.map(function (val) {
                return val / max;
            });
        });

        var chart = new ColumnChart($dataTable.attr('summary'));
        $dataTable.replaceWith(chart.element);
        chart.draw(relativeValues);
    }

    function initBugCountChart() {
        var $dataTable = $('#open-bug-data');

        var data = extractData($dataTable, [parseDate, parseInt]);
        var rawValues = data.map(function (row) {
            // drop date; we don't display it
            return row[1];
        });

        // Normalise values into the range [0, 1]
        var max = Math.max.apply(null, rawValues);
        var relativeValues = rawValues.map(function (val) {
            return val / max;
        });

        var chart = new LineChart($dataTable.attr('summary'));
        $dataTable.replaceWith(chart.element);
        chart.draw(relativeValues);
    }

    // ----------------------------------------
    // Initialisation

    $(function () {
        initBugRateChart();
        initBugCountChart();
        // Refresh every 10 minutes to get latest data
        window.setTimeout(function () { window.location.reload(); }, 1000 * 60 * 10);
    });
}());
