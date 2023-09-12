CREATE TABLE stock_price (
    id serial4 NOT NULL,
    symbol varchar(50) NULL,
    date date NULL,
    open numeric(30,20) NULL,
    next_open numeric(30,20) NULL,
    high numeric(30,20) NULL,
    low numeric(30,20) NULL,
    close numeric(30,20) NULL,
    adj_close numeric(30,20) NULL,
    volume numeric(10,5) NULL,
    cdate timestamptz NOT null default current_timestamp,
    CONSTRAINT stock_price_pkey PRIMARY KEY (id)
);