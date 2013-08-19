var app = app || {};

$(function() {

    // The model for our weigh mapped to the Django one.
    app.Transaction = Backbone.Model.extend({

        url: function() {
            return "/api/1.0/item/"+this.id;
        },

        constructor : function(attrs, options) {
            attrs.selected = false;
            attrs.selectable = true;
            Backbone.Model.call(this, attrs, options);
            var id = this.id;
        }

    });

    // The collection of our transaction models.
    TransactionList = Backbone.Collection.extend({
        model: app.Transaction,

        // A catcher for the meta object TastyPie will return.
        meta: {},

        // Set the (relative) url to the API for the item resource.
        url: "/api/1.0/item/",

        // Our API will return an object with meta, then objects list.
        parse: function(response) {
            this.meta = response.meta;
            return response.objects;
        }
    });
    app.Transactions = new TransactionList();

    // The visual representation of a single model.
    app.TransactionView = Backbone.View.extend({
        // The element we'll append for the collection models.
        tagName: "tr",

        // Cache the template for a single model.
        template: _.template($("#ticket-template").html()),

        // Bind our events.
        events: {
              "click td": "select"
        },

        // Set up our listeners to model events.
        initialize: function() {
            // (re)Render the view when the model changes
            this.listenTo(this.model, "change", this.render);

            // Remove the view when the model is destroyed
            this.listenTo(this.model, "destroy", this.remove);
        },

        // Render our view to the DOM as a new li (from tagName).
        render: function() {
            var _self = this;

            // Give the list item an id.
            this.$el.attr("id", this.model.get("id"));

            // Render the template with our model as a JSON object.
            this.$el.html(this.template(this.model.toJSON()));

            this.$el.toggleClass("selected", this.model.get("selected"));

            return this;
        },

        select: function(){
            this.$el.toggleClass("selected");
            $('#weigh-btn').html('Weigth Out');
        }

    });

    // The view for the entire app.
    app.AppView = Backbone.View.extend({
        el: "#todo-app",

        initialize: function() {
            // TastyPie requires us to use a ?format=json param, so we'll
            // set that as a default.
            $.ajaxPrefilter(function(options) {
                _.extend(options, {format: "json"});
            });

            this.listenTo(app.Transactions, "add", this.addOne);
            this.listenTo(app.Transactions, "reset", this.addAll);

            // Get our transactions from the API!
            app.Transactions.fetch();
        },

        // Add a single to the list.
        addOne: function(transaction) {
            var view = new app.TransactionView({model: transaction});
            $("#ticket-list").append(view.render().el);
        },

        addAll: function() {
            this.$("ticket-list").html("");
            app.Transactions.each(this.addOne, this);
        }
    });

    // And we're off.
    new app.AppView();
});