

select

  ord.*,
  case when brnd.brand_sessions > 0 then 'Yes' when brnd.brand_sessions = 0 then 'No' else 'Unknown' end as branded_traffic

from
  (
    select 
      distinct 
      o.completed_at::date as order_date,
      o.order_number,
      case when o.first_order_number is not null then 'New' else 'Repeat' end as customer_type,
      lower(a.city) as city,
      lower(a.zipcode) as postcode
    from truth.fact_order_items o
    join truth.dim_addresses a
      on a.key = o.bill_address_fk
    where 
      o.bill_country_fk in (select key from truth.dim_countries where name = 'United Kingdom')
      and o.completed_at >= '2016-10-03' 
  ) ord

left join
  (
    select 
      i.next_conversion_number,
      count(distinct case when c.channel in ('ppc_brand','direct','organic') then c.channel else null end) as brand_sessions
    from truth.fact_interactions i
    join truth.dim_ads c
      on c.key = i.ad_fk
    where is_chain_converting and i.timestamp >= '2016-09-01' and attribution_model = 'last'
    group by 1
  ) brnd

on brnd.next_conversion_number = ord.order_number

order by 1,2,4




--limit 1000 
