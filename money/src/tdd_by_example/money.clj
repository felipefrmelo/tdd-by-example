(ns tdd-by-example.money

  (:gen-class))


(defrecord Money [amount])

(defn new-money [amount] (->Money amount))

(def dollar  new-money )

(defn times [money mult] (dollar (* (:amount money) mult)))
